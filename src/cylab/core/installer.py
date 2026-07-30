"""
CYLAB Installer
Installs required tools for the cybersecurity lab.
"""

import shutil
import subprocess


INSTALLERS = {
    "docker": {
        "check": lambda: shutil.which("docker") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "docker.io"],
        ],
    },
    "ollama": {
        "check": lambda: shutil.which("ollama") is not None,
        "commands": [
            ["bash", "-c", "curl -fsSL https://ollama.com/install.sh | sh"],
        ],
    },
    "nmap": {
        "check": lambda: shutil.which("nmap") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "nmap"],
        ],
    },
    "nikto": {
        "check": lambda: shutil.which("nikto") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "nikto"],
        ],
    },
    "gobuster": {
        "check": lambda: shutil.which("gobuster") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "gobuster"],
        ],
    },
    "searchsploit": {
        "check": lambda: shutil.which("searchsploit") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "exploitdb"],
        ],
    },
    "metasploit": {
        "check": lambda: shutil.which("msfconsole") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "metasploit-framework"],
        ],
    },
    "sqlmap": {
        "check": lambda: shutil.which("sqlmap") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "sqlmap"],
        ],
    },
    "hydra": {
        "check": lambda: shutil.which("hydra") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "hydra"],
        ],
    },
    "john": {
        "check": lambda: shutil.which("john") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "john"],
        ],
    },
    "trivy": {
        "check": lambda: shutil.which("trivy") is not None,
        "commands": [
            ["bash", "-c", "curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin"],
        ],
    },
    "theharvester": {
        "check": lambda: shutil.which("theHarvester") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "theharvester"],
        ],
    },
    "spiderfoot": {
        "check": lambda: shutil.which("sf.py") is not None or shutil.which("spiderfoot") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "spiderfoot"],
        ],
    },
    "node": {
        "check": lambda: shutil.which("node") is not None,
        "commands": [
            ["sudo", "apt", "update"],
            ["sudo", "apt", "install", "-y", "nodejs", "npm"],
        ],
    },
}


def is_installed(name: str) -> bool:
    installer = INSTALLERS.get(name)
    if not installer:
        return False
    return installer["check"]()


def install(name: str) -> bool:
    installer = INSTALLERS.get(name)
    if not installer:
        print(f"Unknown package: {name}")
        print(f"Available: {', '.join(INSTALLERS.keys())}")
        return False

    if is_installed(name):
        print(f"{name} is already installed.")
        return True

    print(f"About to install: {name}")
    print("This requires sudo privileges and will run system commands.")
    confirm = input("Continue? [y/N] ")
    if confirm.strip().lower() != "y":
        print("Installation cancelled.")
        return False

    for cmd in installer["commands"]:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"Command failed: {' '.join(cmd)}")
            return False

    if is_installed(name):
        print(f"{name} installed successfully.")
        return True
    else:
        print(f"{name} installation finished but could not be verified.")
        return False
