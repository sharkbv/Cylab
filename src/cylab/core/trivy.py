"""
CYLAB Trivy
Scans Docker images for known vulnerabilities.
"""

import shutil
import subprocess


def trivy_available():
    return shutil.which("trivy") is not None


def scan_image(image, timeout=300):
    if not trivy_available():
        return None

    cmd = ["trivy", "image", "--quiet", image]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

    return result.stdout
