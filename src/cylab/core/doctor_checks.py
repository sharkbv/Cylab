"""
CYLAB Doctor Checks
Shared check logic used by both doctor and report commands.
"""

import platform
import shutil
import sys


def run_checks():
    checks = []

    checks.append({
        "name": f"Python version ({sys.version.split()[0]})",
        "passed": sys.version_info >= (3, 9),
        "hint": "Install Python 3.9 or newer",
    })

    checks.append({
        "name": f"Operating System ({platform.system()})",
        "passed": True,
        "hint": "",
    })

    checks.append({
        "name": "Git installed",
        "passed": shutil.which("git") is not None,
        "hint": "sudo apt install git",
    })

    checks.append({
        "name": "Docker installed",
        "passed": shutil.which("docker") is not None,
        "hint": "cylab install docker",
    })

    checks.append({
        "name": "Ollama installed",
        "passed": shutil.which("ollama") is not None,
        "hint": "cylab install ollama",
    })

    return checks
