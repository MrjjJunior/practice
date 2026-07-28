"""
main.py
-------

    User -> Orchestrator -> System Prompt -> Groq (Llama) -> JSON
          -> Validation -> Dispatcher -> Journey Handler
          -> State Machine -> Backend -> Response -> User

Run it:

    export GROQ_API_KEY="gsk_..."
    pip install -r requirements.txt
    python main.py

Type like a customer ("I was in a car accident yesterday on Main St"),
or type `--trace` at any point to toggle verbose step-by-step logging
of exactly what each layer did (great for demoing to judges).
"""

from validation import get_validated_response
from dispatcher import dispatch

SESSION = {"customer_id": "demo-customer-1"}
SHOW_TRACE = True


def banner():
    print("=" * 64)
    print(" Insurance AI Assistant -- demo (Groq + OpenAI SDK)")
    print(" Type 'quit' to exit. Type '--trace' to toggle verbose mode.")
    print("=" * 64)


def handle_turn(user_message: str):
    print("\n[User]      ", user_message)

    parsed, trace = get_validated_response(user_message)

    if SHOW_TRACE:
        print("\n--- pipeline trace -----------------------------------")
        for line in trace:
            print(" ", line)
        print("-------------------------------------------------------")

    if parsed is None:
        # Every retry failed -- graceful failure, never a crash, never
        # silently guessing what the user meant.
        print("[Assistant] ", "Sorry, I'm having trouble understanding that "
                               "right now. Could you try rephrasing?")
        return

    print(f"[Orchestrator -> Validation] intent={parsed.intent!r} "
          f"confidence={parsed.confidence:.2f}")

    if parsed.intent == "clarify":
        # No business logic to dispatch to -- just ask the question.
        print("[Assistant] ", parsed.clarifying_question)
        return

    print(f"[Dispatcher] routing '{parsed.intent}' to its journey handler...")
    reply = dispatch(parsed.intent, parsed.entities, SESSION)
    print("[Assistant] ", reply)


def main():
    global SHOW_TRACE
    banner()
    while True:
        try:
            user_message = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not user_message:
            continue
        if user_message.lower() in ("quit", "exit"):
            print("Goodbye.")
            break
        if user_message == "--trace":
            SHOW_TRACE = not SHOW_TRACE
            print(f"(trace {'ON' if SHOW_TRACE else 'OFF'})")
            continue

        handle_turn(user_message)


if __name__ == "__main__":
    main()