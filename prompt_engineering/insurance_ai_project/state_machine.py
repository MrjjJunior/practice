"""
state_machine.py
----------------

A state machine's whole job is to say: given where the conversation
currently is, what transitions are actually legal right now?

This is what stops a user from typing "approve my claim now" out of
nowhere and skipping straight to a state they haven't earned. If the
requested transition isn't legal from the current state, we simply stay
put and ask for whatever the current state needs.
"""

from enum import Enum, auto


class ClaimState(Enum):
    START = auto()
    COLLECT_DATE = auto()
    COLLECT_LOCATION = auto()
    COLLECT_DESCRIPTION = auto()
    SUBMITTED = auto()


# Legal transitions: from_state -> {trigger: to_state}
CLAIM_TRANSITIONS = {
    ClaimState.START: {"has_date": ClaimState.COLLECT_DATE},
    ClaimState.COLLECT_DATE: {"date_given": ClaimState.COLLECT_LOCATION},
    ClaimState.COLLECT_LOCATION: {"location_given": ClaimState.COLLECT_DESCRIPTION},
    ClaimState.COLLECT_DESCRIPTION: {"description_given": ClaimState.SUBMITTED},
    ClaimState.SUBMITTED: {},  # terminal state, no further transitions
}


class ClaimStateMachine:
    """
    Tracks one customer's progress through the claim-filing journey and
    decides what the next question should be. Fields collected so far
    are kept in `self.data` (never trusted to the AI to remember).
    """

    def __init__(self):
        self.state = ClaimState.START
        self.data = {"accident_date": None, "location": None, "description": None}

    def next_prompt(self) -> str:
        if self.state == ClaimState.START or self.data["accident_date"] is None:
            return "When did the accident happen?"
        if self.data["location"] is None:
            return "Where did the accident happen?"
        if self.data["description"] is None:
            return "Can you briefly describe what happened?"
        return "Thanks -- I have everything I need to file your claim."

    def advance(self, entities) -> bool:
        """
        Attempt to move forward using whatever entities the AI extracted
        this turn. Returns True if the state advanced, False if the
        transition was illegal (e.g. the user tried to jump ahead) --
        in which case we just stay in the current state and re-ask.
        """
        if self.data["accident_date"] is None and entities.accident_date:
            self.data["accident_date"] = entities.accident_date

        if self.data["accident_date"] is not None and self.data["location"] is None and entities.location:
            self.data["location"] = entities.location

        if (
            self.data["accident_date"] is not None
            and self.data["location"] is not None
            and self.data["description"] is None
            and entities.description
        ):
            self.data["description"] = entities.description

        if all(self.data.values()):
            self.state = ClaimState.SUBMITTED
            return True

        # Recompute a simple linear state for display purposes.
        if self.data["description"]:
            self.state = ClaimState.SUBMITTED
        elif self.data["location"]:
            self.state = ClaimState.COLLECT_DESCRIPTION
        elif self.data["accident_date"]:
            self.state = ClaimState.COLLECT_LOCATION
        else:
            self.state = ClaimState.START

        return self.state == ClaimState.SUBMITTED

    def is_complete(self) -> bool:
        return self.state == ClaimState.SUBMITTED