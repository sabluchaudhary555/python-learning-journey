# py-env-checker 🐍

A simple Python script that checks whether your Python environment is correctly set up — version, pip, virtual environment, installed packages, and requirements.txt.

Built as a learning project while studying Python basics (installation, pip, virtual environments).

---

## What it checks

| # | Check |
|---|---|
| 1 | OS and system info |
| 2 | Python version (warns if < 3.9) |
| 3 | pip availability and version |
| 4 | Whether a virtual environment is active |
| 5 | Presence of common packages (requests, numpy, flask, pandas) |
| 6 | requirements.txt — lists dependencies if file exists |

---

## How to run

```bash
python3 py-env-checker.py
```

No installs needed — uses only the Python standard library.

---

## Sample output

```
==================================================
   Python Environment Checker
==================================================

--------------------------------------------------
[6] SYSTEM INFO
--------------------------------------------------
OS      : Linux 5.15.0
Machine : x86_64
CWD     : /home/user/project

--------------------------------------------------
[1] PYTHON VERSION
--------------------------------------------------
Version   : 3.11.4 (main, Jul 5 2023)
Executable: /usr/bin/python3
OK: Python version looks good.

--------------------------------------------------
[3] VIRTUAL ENVIRONMENT
--------------------------------------------------
WARNING: No virtual environment is active.
TIP: Run  ->  python3 -m venv venv  then  source venv/bin/activate

--------------------------------------------------
[4] PACKAGE CHECK
--------------------------------------------------
  FOUND   requests (2.31.0)
  MISSING numpy  ->  pip install numpy
  FOUND   flask (3.0.0)
  MISSING pandas  ->  pip install pandas

--------------------------------------------------
[5] requirements.txt
--------------------------------------------------
No requirements.txt found in current directory.
TIP: Run  ->  pip freeze > requirements.txt
```

---

## Customise package list

Open the script and edit this list:

```python
packages_to_check = ["requests", "numpy", "flask", "pandas"]
```

Add any package you want to verify.

---

## Concepts covered

- `sys` module — version info, executable path, venv detection
- `subprocess` — running pip commands from Python
- `os` and `platform` — system and directory info
- Virtual environment detection via `sys.prefix vs sys.base_prefix`
- Reading and parsing `requirements.txt`

---

## Requirements

- Python 3.x
- No external libraries — standard library only

---

## Author

**Sabl Chaudhary** — Cybersecurity Lead @ GDSC Purvanchal University
GitHub: [sabluchaudhary555](https://github.com/sabluchaudhary555)
Site: [SSoft.in](https://SSoft.in)