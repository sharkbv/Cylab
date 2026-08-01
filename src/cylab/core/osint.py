"""
CYLAB OSINT
Runs theHarvester and SpiderFoot for information gathering.
"""

import shutil
import subprocess


def theharvester_available():
    return shutil.which("theHarvester") is not None


def spiderfoot_available():
    return shutil.which("sf.py") is not None or shutil.which("spiderfoot") is not None


def run_theharvester(domain, source="all", timeout=600):
    if not theharvester_available():
        return None

    cmd = ["theHarvester", "-d", domain, "-l", "0", "-b", source]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout


def run_spiderfoot(domain, timeout=300):
    binary = shutil.which("sf.py") or shutil.which("spiderfoot")
    if not binary:
        return None

    cmd = [binary, "-s", domain, "-q"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
