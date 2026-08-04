"""
CYLAB Nuclei
Runs Nuclei template-based vulnerability scanning.
"""

import shutil
import subprocess


def nuclei_available():
    return shutil.which("nuclei") is not None


def run_nuclei(target, timeout=300):
    if not nuclei_available():
        return None

    cmd = ["nuclei", "-u", target, "-silent"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
