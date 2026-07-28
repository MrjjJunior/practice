"""
journey_handlers.py
--------------------

A Journey Handler owns the business logic for ONE workflow (filing a
claim, changing an address, checking status). It:
  - talks to its State Machine to figure out what step we're on,
  - talks to the Backend to actually do things (source of truth),
  - returns a plain-English message for the user.

Journey Handlers never talk to the AI. They only ever receive
already-validated data from the Dispatcher.
"""

import backend
from state_machine import ClaimStateMachine


class ClaimJourneyHandler:
    """Handles the multi-turn 'report_claim' journey."""

    def __init__(self, session):
        # Reuse the same state machine across turns for this session.
        if "claim_state_machine" not in session:
            session["claim_state_machine"] = ClaimStateMachine()
        self.machine: ClaimStateMachine = session["claim_state_machine"]
        self.session = session

    def handle(self, entities) -> str:
        completed = self.machine.advance(entities)

        if completed:
            result = backend.create_claim(
                customer_id=self.session["customer_id"],
                accident_date=self.machine.data["accident_date"],
                location=self.machine.data["location"],
                description=self.machine.data["description"],
            )
            # Journey is done -- clear it so a future claim starts fresh.
            self.session.pop("claim_state_machine", None)
            return (
                f"Your claim has been filed. Reference number: "
                f"{result['claim_id']}. Status: {result['status']}."
            )

        return self.machine.next_prompt()


class AddressChangeHandler:
    """Handles the single-turn 'change_address' journey."""

    def __init__(self, session):
        self.session = session

    def handle(self, entities) -> str:
        if not entities.new_address:
            return "Sure -- what's the new address you'd like on file?"
        result = backend.update_address(
            customer_id=self.session["customer_id"],
            new_address=entities.new_address,
        )
        return f"Got it. Your address is now on file as: {result['address']}."


class ClaimStatusHandler:
    """Handles the single-turn 'check_claim_status' journey."""

    def __init__(self, session):
        self.session = session

    def handle(self, entities) -> str:
        result = backend.get_claim_status(
            customer_id=self.session["customer_id"],
            claim_id=entities.claim_id,
        )
        if result.get("status") == "NO_CLAIMS_FOUND":
            return "I don't see any claims on file for you yet."
        return (
            f"Claim {result['claim_id']} is currently: {result['status']}."
        )
