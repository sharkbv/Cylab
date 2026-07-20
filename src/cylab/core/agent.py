"""
CYLAB Agent
Uses a local Ollama model to analyze CYLAB data.
"""

import subprocess
import shutil


def ollama_available():
    return shutil.which("ollama") is not None


def ask_model(model, prompt):
    if not ollama_available():
        return None

    result = subprocess.run(
        ["ollama", "run", model, prompt],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return None

    return result.stdout.strip()


def build_doctor_prompt(report):
    lines = ["Analyze this cybersecurity lab diagnostic report."]
    lines.append(f"Passed: {report.get('passed')}/{report.get('total')}")
    lines.append("")

    for check in report.get("checks", []):
        status = "OK" if check["passed"] else "FAILED"
        lines.append(f"- {check['name']}: {status}")
        if not check["passed"] and check.get("hint"):
            lines.append(f"  suggested fix: {check['hint']}")

    lines.append("")
    lines.append(
        "Give a short, practical summary and prioritize what to fix first."
    )

    return "\n".join(lines)
