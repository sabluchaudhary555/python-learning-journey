# Python — Introduction & Installation
> Quick reference notes | Source: GFG

---

## 1. What is Python?

Python is a **high-level, interpreted, general-purpose** programming language created by **Guido van Rossum** in **1991**.

| Feature | Description |
|---|---|
| Syntax | Simple, readable — close to plain English |
| Typing | Dynamically typed — no type declarations needed |
| Execution | Interpreted — runs line by line, no compilation |
| Paradigms | Procedural, OOP, Functional |
| Memory | Automatic garbage collection |
| Platform | Cross-platform — Windows, macOS, Linux |

### Programming Paradigms

| Paradigm | Description | Example Use |
|---|---|---|
| Procedural | Step-by-step instructions | Scripts, automation |
| OOP | Classes and objects | Web apps, games |
| Functional | Functions as first-class citizens | Data pipelines |

---

## 2. History

| Year | Event |
|---|---|
| 1989 | Guido started developing Python |
| 1991 | Python 1.0 released |
| 2000 | Python 2.0 — list comprehensions, GC |
| 2008 | Python 3.0 — major redesign, not backward compatible |
| 2018 | Guido stepped down as BDFL; steering council formed |
| 2020 | Python 2 officially End of Life |
| Now | Python 3.x only |

> Named after **Monty Python's Flying Circus** — not the snake.

---

## 3. Where is Python Used?

| Domain | Libraries/Frameworks |
|---|---|
| Web Development | Django, Flask, FastAPI |
| Data Science | Pandas, NumPy, Matplotlib |
| ML / AI | TensorFlow, PyTorch, Scikit-learn |
| Automation | os, shutil, subprocess |
| Cybersecurity | Scapy, socket |
| Web Scraping | BeautifulSoup, Scrapy, Selenium |
| Desktop GUI | Tkinter, PyQt, CustomTkinter |
| DevOps / Cloud | Ansible, Boto3 |
| IoT | MicroPython, Raspberry Pi |

---

## 4. Python vs Other Languages

| Feature | Python | Java | C++ | JavaScript |
|---|---|---|---|---|
| Syntax | Simple | Verbose | Complex | Moderate |
| Typing | Dynamic | Static | Static | Dynamic |
| Speed | Moderate | Fast | Very Fast | Moderate |
| Memory | Auto (GC) | Auto (GC) | Manual | Auto (GC) |
| Learning Curve | Low | Medium | High | Low-Medium |

---

## 5. Hello World

```python
# This is a comment
print("Hello, World!")
```

Output:
```
Hello, World!
```

- `print()` is a built-in function
- Strings use single `'` or double `"` quotes

---

## 6. Installation

### Windows
1. Download from [python.org](https://python.org)
2. Run `.exe` installer
3. ✅ Check **"Add Python to PATH"** — important
4. Click Install Now

### macOS
```bash
brew install python3
```

### Linux (Debian/Ubuntu)
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Verify
```bash
python3 --version     # macOS / Linux
python --version      # Windows

# Output: Python 3.x.x
```

---

## 7. pip — Package Manager

pip comes with Python 3.4+. It installs packages from **PyPI**.

```bash
pip --version                        # check version

pip install requests                 # install a package
pip install requests==2.31.0         # specific version
pip install "requests>=2.0"          # minimum version

pip list                             # list installed packages
pip show requests                    # package details
pip uninstall requests               # remove package
pip install --upgrade requests       # upgrade package
pip install --upgrade pip            # upgrade pip itself
```

### requirements.txt

```bash
pip freeze > requirements.txt        # export dependencies
pip install -r requirements.txt      # install from file
```

Sample `requirements.txt`:
```
requests==2.31.0
numpy>=1.24.0
flask
```

---

## 8. Virtual Environments

A **virtual environment** = isolated Python environment per project.
Prevents version conflicts between projects.

```bash
# Create
python3 -m venv venv

# Activate
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# Prompt changes to:
# (venv) user@machine:~/project$

# Install packages (only inside this env)
pip install flask

# Deactivate
deactivate
```

### Best Practices

| Practice | Recommendation |
|---|---|
| One per project | Separate venv for each project |
| Name consistently | Use `venv`, `.venv`, or `env` |
| Gitignore | Never commit venv folder |
| Document deps | Always maintain `requirements.txt` |

`.gitignore` entries:
```
venv/
.venv/
env/
__pycache__/
*.pyc
```

---

## 9. IDEs & Editors

| Tool | Best For |
|---|---|
| **VS Code** | General dev, scripting, automation, web |
| **PyCharm** | Large projects, Django/Flask, professional |
| **Jupyter Notebook** | Data science, ML, experimentation |

### Jupyter Notebook

```bash
pip install jupyter
jupyter notebook        # opens at http://localhost:8888
```

Key shortcuts:
| Shortcut | Action |
|---|---|
| `Shift + Enter` | Run cell, move to next |
| `Ctrl + Enter` | Run cell |
| `A` | Insert cell above |
| `B` | Insert cell below |
| `DD` | Delete cell |

---

## Quick Cheat Sheet

```bash
# INSTALLATION
python3 --version                    # verify install
which python3                        # find location (Linux/Mac)
where python                         # find location (Windows)

# PIP
pip install <package>                # install
pip uninstall <package>              # remove
pip list                             # list all installed
pip freeze > requirements.txt        # export deps
pip install -r requirements.txt      # install from file

# VIRTUAL ENV
python3 -m venv venv                 # create
source venv/bin/activate             # activate (Linux/Mac)
venv\Scripts\activate                # activate (Windows)
deactivate                           # deactivate

# FIRST PROGRAM
python3 hello.py                     # run a script
python3                              # open interactive shell
>>> exit()                           # exit shell
```