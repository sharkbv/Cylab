"""
CYLAB Fuzzer
Runs ffuf for fast web fuzzing (directories, parameters, subdomains).
"""

import shutil
import subprocess


def ffuf_available():
    return shutil.which("ffuf") is not None


def run_ffuf(url, wordlist="/usr/share/wordlists/dirb/common.txt", timeout=300):
    if not ffuf_available():
        return None

    if "FUZZ" not in url:
        url = url.rstrip("/") + "/FUZZ"

    cmd = ["ffuf", "-u", url, "-w", wordlist, "-mc", "200,204,301,302,307,401,403", "-s"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
