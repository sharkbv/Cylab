"""
CYLAB Metasploit
Searches Metasploit modules via msfconsole.
"""

import shutil
import subprocess


def msf_available():
    return shutil.which("msfconsole") is not None


def search_modules(query, timeout=120):
    if not msf_available():
        return None

    cmd = ["msfconsole", "-q", "-x", f"search {query}; exit"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
