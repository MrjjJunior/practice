"""
validation.py
--------------

This is the gate between the AI and the rest of the system. Nothing
reaches the dispatcher unless it passes through here successfully.

Two failure modes we defend against:
  1. Malformed JSON (the model didn't return parseable JSON at all).
  2. Well-formed but semantically invalid JSON (unknown intent, missing
     fields, confidence out of range, etc. -- caught by the pydantic
     schema in schemas.py).
"""

import json
from typing import Tuple, Optional
from pydantic import ValidationError

from schemas import AIResponse, CONFIDENCE_THRESHOLD
from orchestrator import call_model

MAX_RETRIES = 2


def validate_json(raw_text: str) -> Tuple[Optional[AIResponse], Optional[str]]:
    """
    Try to turn raw model output into a validated AIResponse.
    Returns (response, None) on success, or (None, error_message) on failure.
    """
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as e:
        return None, f"not valid JSON ({e})"

    try:
        parsed = AIResponse(**data)
    except ValidationError as e:
        return None, f"JSON did not match required schema ({e.errors()[0]['msg']})"

    return parsed, None


def get_validated_response(user_message: str) -> Tuple[Optional[AIResponse], list]:
    """
        call model -> validate -> if invalid, re-prompt with the error
        -> validate again -> ... -> give up gracefully after MAX_RETRIES

    Returns (validated_response_or_None, trace) where trace is a list of
    human-readable strings describing what happened at each attempt, so
    the demo/CLI can print exactly what the system did.
    """
    trace = []
    retry_hint = ""

    for attempt in range(1, MAX_RETRIES + 2):  # first try + MAX_RETRIES retries
        trace.append(f"Attempt {attempt}: calling model...")
        raw = call_model(user_message, retry_hint=retry_hint)
        trace.append(f"Attempt {attempt}: raw model output -> {raw!r}")

        parsed, error = validate_json(raw)
        if parsed is not None:
            trace.append(f"Attempt {attempt}: validation PASSED.")

            # Confidence gate: even a structurally valid response gets
            # downgraded to "clarify" if the model wasn't confident enough.
            if parsed.intent != "clarify" and parsed.confidence < CONFIDENCE_THRESHOLD:
                trace.append(
                    f"Confidence {parsed.confidence:.2f} below threshold "
                    f"{CONFIDENCE_THRESHOLD} -> forcing 'clarify'."
                )
                parsed.intent = "clarify"
                parsed.clarifying_question = (
                    parsed.clarifying_question
                    or "Could you tell me a bit more about what you need?"
                )
            return parsed, trace

        trace.append(f"Attempt {attempt}: validation FAILED -> {error}")
        retry_hint = error

    trace.append("All retries exhausted -> graceful failure.")
    return None, trace