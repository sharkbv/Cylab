"""
CYLAB Scan Store
Saves and reads per-target, per-tool scan results.
Each tool's result for a target overwrites the previous one (current state only).
"""

import re
from pathlib import Path

SCANS_DIR = Path.home() / ".cylab" / "scans"
LAST_TARGET_FILE = Path.home() / ".cylab" / "last_target"


def safe_target_name(target):
    name = target.replace("http://", "").replace("https://", "")
    name = re.sub(r"[^a-zA-Z0-9._-]", "_", name)
    return name


def save_result(target, tool, output):
    folder = SCANS_DIR / safe_target_name(target)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{tool}.txt").write_text(output or "")
    LAST_TARGET_FILE.parent.mkdir(parents=True, exist_ok=True)
    LAST_TARGET_FILE.write_text(target)


def get_last_target():
    if not LAST_TARGET_FILE.exists():
        return None
    return LAST_TARGET_FILE.read_text().strip()


def list_target_results(target):
    folder = SCANS_DIR / safe_target_name(target)
    if not folder.exists():
        return {}
    results = {}
    for f in folder.glob("*.txt"):
        results[f.stem] = f.read_text()
    return results


def build_target_summary(target):
    results = list_target_results(target)
    if not results:
        return None

    parts = [f"=== Target: {target} ===\n"]
    labels = {
        "nmap": "Nmap (open ports/services)",
        "webscan": "Web Scan (Nikto/Gobuster)",
        "nuclei": "Nuclei (vulnerability templates)",
        "searchsploit": "Known Exploits (searchsploit)",
        "msf": "Metasploit (matching modules)",
    }

    for tool, label in labels.items():
        if tool in results and results[tool].strip():
            parts.append(f"[{label}]\n{results[tool].strip()}\n")

    return "\n".join(parts)
