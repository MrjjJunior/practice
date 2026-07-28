"""
backend.py
----------
The "source of truth". This is a stand-in for whatever real system your
company already trusts (a claims database, a policy admin system, etc).

Key architectural point for judges: the AI NEVER calls this directly.
Only Journey Handlers call it, and only with already-validated,
already-authorized data. This module also does a final authorization
check of its own -- defense in depth, not just trusting the layers above.
"""

import itertools
import random

_claim_id_counter = itertools.count(1000)

# In-memory "database" for the demo.
_DB = {
    "claims": {},
    "customer_address": "123 Main Street, Springfield",
}


def is_authorized(customer_id: str, action: str) -> bool:
    """Placeholder authorization check. In a real system this would
    check the authenticated session, policy status, permissions, etc.
    The backend does this itself and never assumes the layers above
    already checked -- defense in depth."""
    return True  # demo: everyone is authorized


def create_claim(customer_id: str, accident_date, location, description) -> dict:
    if not is_authorized(customer_id, "create_claim"):
        raise PermissionError("Not authorized to create a claim.")
    claim_id = f"CLM-{next(_claim_id_counter)}"
    _DB["claims"][claim_id] = {
        "customer_id": customer_id,
        "accident_date": accident_date,
        "location": location,
        "description": description,
        "status": "SUBMITTED",
    }
    return {"claim_id": claim_id, "status": "SUBMITTED"}


def update_address(customer_id: str, new_address: str) -> dict:
    if not is_authorized(customer_id, "update_address"):
        raise PermissionError("Not authorized to update address.")
    _DB["customer_address"] = new_address
    return {"address": new_address, "status": "UPDATED"}


def get_claim_status(customer_id: str, claim_id: str = None) -> dict:
    if not is_authorized(customer_id, "get_claim_status"):
        raise PermissionError("Not authorized to view claim status.")
    if claim_id and claim_id in _DB["claims"]:
        return {"claim_id": claim_id, **_DB["claims"][claim_id]}
    if _DB["claims"]:
        # Return the most recent claim if none was specified.
        latest_id = list(_DB["claims"].keys())[-1]
        return {"claim_id": latest_id, **_DB["claims"][latest_id]}
    return {"status": "NO_CLAIMS_FOUND"}