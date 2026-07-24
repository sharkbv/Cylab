"""
CYLAB Plugins
Discovers and runs user-provided plugin scripts.
"""

import importlib.util
from pathlib import Path

PLUGINS_DIR = Path.home() / ".cylab" / "plugins"


def discover_plugins():
    if not PLUGINS_DIR.exists():
        return {}

    plugins = {}
    for file in PLUGINS_DIR.glob("*.py"):
        name = file.stem
        plugins[name] = file

    return plugins


def load_plugin(name):
    plugins = discover_plugins()
    path = plugins.get(name)
    if not path:
        return None

    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_plugin(name, args):
    module = load_plugin(name)
    if module is None:
        return False

    if not hasattr(module, "run"):
        return False

    module.run(args)
    return True
