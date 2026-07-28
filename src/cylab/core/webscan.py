"""
CYLAB Web Scanner
Runs Nikto and Gobuster against a web target.
"""

import shutil
import subprocess


def nikto_available():
    return shutil.which("nikto") is not None


def gobuster_available():
    return shutil.which("gobuster") is not None


def run_nikto(target, timeout=300):
    if not nikto_available():
        return None

    cmd = ["nikto", "-h", target, "-ask", "no"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout


def run_gobuster(target, wordlist="/usr/share/wordlists/dirb/common.txt", timeout=300):
    if not gobuster_available():
        return None

    cmd = ["gobuster", "dir", "-u", target, "-w", wordlist, "-q"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
