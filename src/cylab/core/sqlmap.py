"""
CYLAB SQLMap
Runs SQLMap against a target URL for SQL injection testing.
"""

import shutil
import subprocess


def sqlmap_available():
    return shutil.which("sqlmap") is not None


def run_sqlmap(target, timeout=300):
    if not sqlmap_available():
        return None

    cmd = ["sqlmap", "-u", target, "--batch", "--random-agent"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
