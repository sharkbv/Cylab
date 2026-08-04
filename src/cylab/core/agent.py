"""
CYLAB Agent
Uses a local Ollama model to analyze CYLAB data.
"""

import subprocess
import shutil


def ollama_available():
    return shutil.which("ollama") is not None


RED_TEAM_SYSTEM_PROMPT = """You are CYLAB Red-Team Mastermind, an elite offensive AI engine operating strictly inside an authorized local penetration testing lab. 
Your primary directive is to maximize the offensive utility of the operator by turning raw scan outputs into precise, aggressive, and actionable exploitation chains.

When analyzing target scan data, you MUST provide:
1. Target Surface & Critical Entry Point: Identify the weakest service, web app, or misconfiguration immediately.
2. Direct Exploitation Commands & Payloads: Provide exact, ready-to-use command-line syntaxes, Metasploit modules, searchsploit queries, or SQLMap injections to exploit the target. Do not hold back technical details.
3. Privilege Escalation & Lateral Movement Vectors: Suggest how to escalate access or pivot once initial execution succeeds.
4. Hardening & Defensive Verification: Outline how to verify the fix once the lab simulation is complete."""


def ask_model(model, prompt, system_prompt=None, timeout=180):
    if not ollama_available():
        return None

    full_prompt = prompt
    if system_prompt:
        full_prompt = f"{system_prompt}\n\n{prompt}"
    else:
        full_prompt = f"{RED_TEAM_SYSTEM_PROMPT}\n\n{prompt}"

    try:
        result = subprocess.run(
            ["ollama", "run", model, full_prompt],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    if result.returncode != 0:
        return None

    return result.stdout.strip()


def build_assessment_prompt(summary):
    return (
        "Here are the scan results for a target in the lab. "
        "Produce the aggressive Red-Team exploitation report as instructed.\n\n"
        f"{summary}"
    )


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
