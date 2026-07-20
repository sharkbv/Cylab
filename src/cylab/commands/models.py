"""
CYLAB Models Command
"""

from cylab.core.models import (
    ollama_available,
    list_models,
    pull_model,
    run_model,
)


def run(args):
    if not ollama_available():
        print("Ollama is not installed.")
        print("Run: cylab install ollama")
        return

    action = args.models_action

    if action == "list":
        output = list_models()
        if output:
            print(output)
        else:
            print("No models found or Ollama service is not running.")

    elif action == "pull":
        if not args.name:
            print("Usage: cylab models pull <name>")
            return
        print(f"Pulling model: {args.name}")
        ok = pull_model(args.name)
        if ok:
            print(f"Model '{args.name}' pulled successfully.")
        else:
            print(f"Failed to pull model '{args.name}'.")

    elif action == "run":
        if not args.name:
            print("Usage: cylab models run <name>")
            return
        run_model(args.name)

    else:
        print("Usage: cylab models [list|pull <name>|run <name>]")
