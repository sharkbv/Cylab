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

        from cylab.core.scanstore import build_target_summary, get_last_target
        
        # تحديد الهدف (سواء تم تمريره أو جلب آخر هدف مفحوص)
        target = getattr(args, 'target', None)
        if not target:
            target = get_last_target()
            
        if not target:
            print("No target specified and no recent scan found. Run 'cylab scan <target>' or 'cylab assess <target>' first.")
            return

        print(f"[*] Building aggressive exploitation summary for target: {target}")
        summary = build_target_summary(target)
        
        if not summary or "No scan results found" in str(summary):
            print(f"No scan results found for target '{target}'.")
            return

        prompt = build_assessment_prompt(summary)
        model = args.model or "llama3.2"
        
        print(f"Asking {model} to generate the Red-Team exploitation and analysis report...")
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
