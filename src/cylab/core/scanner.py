"""
CYLAB Scanner
Runs Nmap scans safely with sensible defaults.
"""

import shutil
import subprocess

SCAN_PROFILES = {
    "quick": ["-T4", "-F"],
    "full": ["-T4", "-A", "-p-"],
}


def nmap_available():
    return shutil.which("nmap") is not None


def run_scan(target, profile="quick", timeout=300):
    if not nmap_available():
        return None

    flags = SCAN_PROFILES.get(profile, SCAN_PROFILES["quick"])
    cmd = ["nmap"] + flags + [target]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    if result.returncode != 0:
        return None

    return result.stdout
