"""
dispatcher.py
-------------

A tiny, boring, extremely important piece: it maps a validated intent
string to the ONE journey handler responsible for it. Nothing else.
No business logic lives here -- that's the handlers' job. If the
intent isn't in this map, it never got dispatched in the first place
(and validation.py guarantees it can't be an intent outside our allowed
set anyway).
"""

from journey_handlers import (
    ClaimJourneyHandler,
    AddressChangeHandler,
    ClaimStatusHandler,
)

_HANDLER_MAP = {
    "report_claim": ClaimJourneyHandler,
    "change_address": AddressChangeHandler,
    "check_claim_status": ClaimStatusHandler,
}


def dispatch(intent: str, entities, session) -> str:
    """
    Looks up the right Journey Handler class for `intent`, instantiates
    it with the current session, and runs it.

    `intent == "clarify"` never reaches here -- main.py handles that
    case directly by asking the clarifying question, since there's no
    business logic to dispatch to.
    """
    handler_cls = _HANDLER_MAP.get(intent)
    if handler_cls is None:
        # Defense in depth: should be unreachable because validation.py
        # already rejects unknown intents, but we never trust a single
        # layer alone.
        return "Sorry, I'm not able to help with that yet."

    handler = handler_cls(session)
    return handler.handle(entities)