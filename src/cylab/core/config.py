"""
CYLAB Config
Handles loading and saving user configuration.
"""

import tomllib
from pathlib import Path

CONFIG_DIR = Path.home() / ".cylab"
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "default_profile": "default",
}


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        return DEFAULT_CONFIG.copy()

    with open(CONFIG_FILE, "rb") as f:
        data = tomllib.load(f)

    config = DEFAULT_CONFIG.copy()
    config.update(data)
    return config


def save_config(config: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    lines = []
    for key, value in config.items():
        if isinstance(value, str):
            lines.append(f'{key} = "{value}"')
        elif isinstance(value, bool):
            lines.append(f"{key} = {str(value).lower()}")
        else:
            lines.append(f"{key} = {value}")

    CONFIG_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def get_config_path() -> Path:
    return CONFIG_FILE
