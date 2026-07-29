"""
CYLAB Password Auditing
Wraps Hydra (network brute-force) and John the Ripper / Hashcat (hash cracking).
"""

import shutil
import subprocess


def hydra_available():
    return shutil.which("hydra") is not None


def john_available():
    return shutil.which("john") is not None


def hashcat_available():
    return shutil.which("hashcat") is not None


def run_hydra(target, service, userlist, passlist, timeout=300):
    if not hydra_available():
        return None

    cmd = ["hydra", "-L", userlist, "-P", passlist, target, service]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout


def run_john(hash_file, timeout=300):
    if not john_available():
        return None

    cmd = ["john", hash_file]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
