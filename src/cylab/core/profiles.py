"""
CYLAB Profiles
Manages isolated work environments (profiles).
Each profile has its own config file under ~/.cylab/profiles/<name>.toml
"""

import tomllib
from pathlib import Path

PROFILES_DIR = Path.home() / ".cylab" / "profiles"
ACTIVE_PROFILE_FILE = Path.home() / ".cylab" / "active_profile"

DEFAULT_PROFILE_DATA = {
    "log_level": "INFO",
    "description": "Default CYLAB profile",
}


def _profile_path(name: str) -> Path:
    return PROFILES_DIR / f"{name}.toml"


def list_profiles() -> list:
    if not PROFILES_DIR.exists():
        return []
    return sorted(p.stem for p in PROFILES_DIR.glob("*.toml"))


def profile_exists(name: str) -> bool:
    return _profile_path(name).exists()


def create_profile(name: str, description: str = "") -> bool:
    PROFILES_DIR.mkdir(parents=True, exist_ok=True)

    if profile_exists(name):
        return False

    data = DEFAULT_PROFILE_DATA.copy()
    if description:
        data["description"] = description

    lines = []
    for key, value in data.items():
        lines.append(f'{key} = "{value}"')

    _profile_path(name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def load_profile(name: str) -> dict:
    path = _profile_path(name)
    if not path.exists():
        return {}
    with open(path, "rb") as f:
        return tomllib.load(f)


def get_active_profile() -> str:
    if not ACTIVE_PROFILE_FILE.exists():
        return "default"
    return ACTIVE_PROFILE_FILE.read_text(encoding="utf-8").strip()


def set_active_profile(name: str) -> bool:
    if not profile_exists(name):
        return False
    ACTIVE_PROFILE_FILE.parent.mkdir(parents=True, exist_ok=True)
    ACTIVE_PROFILE_FILE.write_text(name, encoding="utf-8")
    return True
