"""
CYLAB Advisor
Combines scan results and asks the AI model for next-step suggestions.
"""

from pathlib import Path

SCANS_DIR = Path.home() / ".cylab" / "scans"


def save_scan_output(name, output):
    SCANS_DIR.mkdir(parents=True, exist_ok=True)
    path = SCANS_DIR / f"{name}.txt"
    path.write_text(output)


def load_scan_output(name):
    path = SCANS_DIR / f"{name}.txt"
    if not path.exists():
        return None
    return path.read_text()


def build_advisor_prompt():
    sections = []
    found_any = False

    for name, label in [("nmap", "Nmap scan"), ("nikto", "Nikto scan"), ("gobuster", "Gobuster scan")]:
        content = load_scan_output(name)
        if content:
            found_any = True
            sections.append(f"--- {label} results ---\n{content.strip()}\n")

    if not found_any:
        return None

    prompt = "You are a security analyst assistant. Here are recent scan results:\n\n"
    prompt += "\n".join(sections)
    prompt += (
        "\nBased on these results, suggest the most likely next steps for a "
        "security assessment. Be specific and prioritize the most impactful findings. "
        "Keep the answer concise and practical."
    )
    return prompt
