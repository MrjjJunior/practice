"""
schemas.py
----------
The single source of truth for what a "valid" AI response looks like.

This is the contract between the AI and the rest of the system. The AI
NEVER talks to the backend directly — it only produces JSON that matches
this contract, and everything downstream is built to trust *only* JSON
that passes validation against this schema.
"""

from typing import Optional
from pydantic import BaseModel, Field, field_validator

# The only intents our system knows how to handle. Anything else is
# rejected by validation and never reaches the dispatcher.
ALLOWED_INTENTS = {
    "report_claim",
    "change_address",
    "check_claim_status",
    "clarify",  # AI is unsure and wants to ask a follow-up question
}

# Minimum confidence the model must report before we'll act on an intent.
# Below this, we force a clarification turn instead of dispatching.
CONFIDENCE_THRESHOLD = 0.55


class Entities(BaseModel):
    """Free-form slots the model may have extracted from the message."""
    accident_date: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    new_address: Optional[str] = None
    claim_id: Optional[str] = None


class AIResponse(BaseModel):
    """
    The exact JSON shape we require Claude/Groq to return.

    Anything that doesn't parse into this shape — or that fails the
    field validators below — is treated as invalid output and triggers
    the retry flow, never the dispatcher.
    """
    intent: str
    confidence: float = Field(ge=0.0, le=1.0)
    entities: Entities = Field(default_factory=Entities)
    clarifying_question: Optional[str] = None

    @field_validator("intent")
    @classmethod
    def intent_must_be_known(cls, v: str) -> str:
        if v not in ALLOWED_INTENTS:
            raise ValueError(
                f"Unknown intent '{v}'. Must be one of {sorted(ALLOWED_INTENTS)}"
            )
        return v


JSON_SCHEMA_FOR_PROMPT = """
{
  "intent": "report_claim | change_address | check_claim_status | clarify",
  "confidence": 0.0-1.0,
  "entities": {
    "accident_date": string or null,
    "location": string or null,
    "description": string or null,
    "new_address": string or null,
    "claim_id": string or null
  },
  "clarifying_question": string or null
}
"""