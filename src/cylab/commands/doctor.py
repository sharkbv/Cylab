"""
CYLAB Doctor Command
Diagnoses the system for CYLAB requirements.
"""

import platform
import shutil
import sys


def check(name: str, condition: bool, hint: str = "") -> bool:
    status = "OK " if condition else "FAIL"
    print(f"[{status}] {name}")
    if not condition and hint:
        print(f"       Fix: {hint}")
    return condition


def run(args) -> None:
    print("Running CYLAB Doctor...\n")

    results = []

    results.append(check(
        f"Python version ({sys.version.split()[0]})",
        sys.version_info >= (3, 9),
        "Install Python 3.9 or newer"
    ))

    results.append(check(
        f"Operating System ({platform.system()})",
        True
    ))

    results.append(check(
        "Git installed",
        shutil.which("git") is not None,
        "sudo apt install git"
    ))

    results.append(check(
        "Docker installed",
        shutil.which("docker") is not None,
        "cylab install docker"
    ))

    results.append(check(
        "Ollama installed",
        shutil.which("ollama") is not None,
        "cylab install ollama"
    ))

    total = len(results)
    passed = sum(results)
    print(f"\n{passed}/{total} checks passed")
