"""
CYLAB Agent Command
"""

from cylab.core.agent import ollama_available, ask_model, build_doctor_prompt
from cylab.core.reports import load_latest_report
from cylab.core.advisor import build_advisor_prompt


def run(args):
    action = args.agent_action

    if action == "analyze":
        if not ollama_available():
            print("Ollama is not installed.")
            print("Run: cylab install ollama")
            return

        report = load_latest_report()
        if not report:
            print("No reports found. Run 'cylab report generate' first.")
            return

        model = args.model or "llama3.2"
        prompt = build_doctor_prompt(report)

        print(f"Asking {model} to analyze the latest report...\n")
        answer = ask_model(model, prompt)

        if answer is None:
            print("Could not get a response from the model.")
            print(f"Make sure the model is pulled: cylab models pull {model}")
            return

        print(answer)

    elif action == "advise":
        if not ollama_available():
            print("Ollama is not installed.")
            print("Run: cylab install ollama")
            return

        prompt = build_advisor_prompt()
        if prompt is None:
            print("No scan results found. Run 'cylab scan' or 'cylab webscan' first.")
            return

        model = args.model or "llama3.2"
        print(f"Asking {model} to suggest next steps based on scan results...")
        print("This may take a minute or two.\n")

        answer = ask_model(model, prompt)

        if answer == "TIMEOUT":
            print("The model took too long to respond.")
            return

        if answer is None:
            print("Could not get a response from the model.")
            return

        print(answer)

    else:
        print("Usage: cylab agent analyze [--model <name>]")
