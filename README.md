# 🔐 Password Generator

[![CI](https://github.com/FrancescoCastaldi/password-generator/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/FrancescoCastaldi/password-generator/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows-lightgrey?logo=apple)]()
[![Security: CSPRNG](https://img.shields.io/badge/security-CSPRNG-critical?logo=lock)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A lightweight, cross-platform desktop application to generate cryptographically secure passwords using common algorithms.

## Features

- Generates **32-character** passwords (256-bit entropy)
- Supports multiple algorithms: `secrets`, `os.urandom`, `UUID4`
- Simple and clean **Tkinter** GUI
- Copy to clipboard with one click
- Works on **macOS** and **Windows**

## Project Structure

```
password-generator/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── generator.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_generator.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10+
- No external dependencies (only stdlib + `pyperclip` for clipboard)

## Installation & Run

### macOS

```bash
git clone https://github.com/FrancescoCastaldi/password-generator.git
cd password-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/app.py
```

> **Note (macOS):** If Tkinter is missing:
> ```bash
> brew install tcl-tk
> brew install python-tk@3.11
> ```

### Windows

```powershell
git clone https://github.com/FrancescoCastaldi/password-generator.git
cd password-generator
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/app.py
```

> **Note (Windows):** Tkinter is bundled with the official Python installer from [python.org](https://www.python.org/downloads/). Reinstall Python and check **"tcl/tk and IDLE"** if missing.

## Running Tests

```bash
python -m pytest tests/ -v
```

## Algorithms Used

| Algorithm | Source | Notes |
|---|---|---|
| `secrets.token_hex` | Python stdlib | CSPRNG, recommended for security |
| `os.urandom + sha256` | OS-level entropy | Direct OS CSPRNG + SHA-256 hash |
| `UUID4` | Python stdlib | Random UUID, 122 bits of entropy |

## License

MIT
