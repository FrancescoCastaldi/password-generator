# 🔐 Password Generator

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
├── src/
│   ├── __init__.py
│   ├── app.py            # Main UI entrypoint
│   ├── generator.py      # Password generation logic
│   └── utils.py          # Clipboard and helper utilities
├── tests/
│   ├── __init__.py
│   └── test_generator.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.9+
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

> **Note (macOS):** If Tkinter is missing, install it via Homebrew:
> ```bash
> brew install python-tk
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

> **Note (Windows):** Tkinter is bundled with the official Python installer from [python.org](https://www.python.org/downloads/). If missing, reinstall Python and check "tcl/tk and IDLE" during setup.

## Running Tests

```bash
python -m pytest tests/ -v
```

## Algorithms Used

| Algorithm | Source | Notes |
|---|---|---|
| `secrets.token_hex` | Python stdlib | CSPRNG, recommended for security |
| `os.urandom` | OS-level entropy | Direct OS CSPRNG |
| `UUID4` | Python stdlib | Random UUID, 122 bits of entropy |

## License

MIT
