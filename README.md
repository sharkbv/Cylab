# CYLAB — Cyber AI Laboratory

CYLAB is a unified command-line platform for managing an AI-powered cybersecurity lab. Instead of juggling dozens of separate tools and scripts, CYLAB gives you one consistent interface to diagnose, configure, install, and organize your lab environment.

```bash
cylab doctor
cylab install docker
cylab profile use pentest-client-a
cylab config show
```

## Why CYLAB?

Most cybersecurity lab setups rely on scattered shell scripts, manual tool installs, and no consistent way to manage multiple engagements or environments. CYLAB solves this with:

- **One CLI** for every lab management task
- **Doctor** — instant environment diagnostics with actionable fixes
- **Profiles** — isolated environments per engagement (client work, CTF, red team, research)
- **Safe installer** — installs required tools with explicit consent, never silent `sudo`
- **Structured logging** — every action is logged to `~/.cylab/logs/cylab.log`

## Installation

Requires Python 3.9+.

```bash
git clone <your-repo-url> cylab
cd cylab
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

Verify:
```bash
cylab --version
```

## Commands

### `cylab doctor`
Diagnoses your environment: Python version, OS, Git, Docker, Ollama. Each failed check comes with a suggested fix.

```bash
cylab doctor
```

### `cylab install <target>`
Installs a required tool (`docker`, `ollama`, `node`). Always asks for explicit confirmation before running any `sudo` command.

```bash
cylab install docker
```

### `cylab config`
Manages global configuration stored at `~/.cylab/config.toml`.

```bash
cylab config show
cylab config set log_level DEBUG
```

### `cylab profile`
Manages isolated work environments. Each profile has its own settings file under `~/.cylab/profiles/<name>.toml`.

```bash
cylab profile create pentest-client-a --description "Client A engagement"
cylab profile list
cylab profile use pentest-client-a
cylab profile show
```

## Project Status

CYLAB is under active development (v1.0, targeting a 15-day build cycle). Current status:

| Module | Status |
|---|---|
| CLI | Done |
| Logger | Done |
| Config | Done |
| Doctor | Done |
| Installer | Done |
| Profiles | Done |
| Reports | In progress |

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for design details and [`CHANGELOG.md`](CHANGELOG.md) for release history.

## Out of scope for v1.0

The following are planned for v2.0 and are intentionally not part of this release:

- Graphical interface / web dashboard
- AI Agents / MCP integration
- Direct Burp Suite / Nmap automation

## License

MIT — see [`LICENSE`](LICENSE).
