"""
CYLAB Models
Manages local Ollama models.
"""

import subprocess
import shutil


def ollama_available():
    return shutil.which("ollama") is not None


def list_models():
    if not ollama_available():
        return None
    result = subprocess.run(
        ["ollama", "list"], capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def pull_model(name):
    if not ollama_available():
        return False
    result = subprocess.run(["ollama", "pull", name])
    return result.returncode == 0


def run_model(name):
    if not ollama_available():
        return False
    subprocess.run(["ollama", "run", name])
    return True
