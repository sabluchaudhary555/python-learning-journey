# Introduction & Installation of Python — Short Notes

## 1. What is Python?
- High-level, interpreted, general-purpose language created by **Guido van Rossum in 1991**.
- Focuses on readability & simplicity — fewer lines than C++/Java.

**Key Characteristics:**
- Simple & readable syntax (like plain English)
- Dynamically typed — no explicit type declarations
- Interpreted — runs line-by-line, no compilation
- Multi-paradigm — procedural, OOP, functional
- Automatic garbage collection
- Cross-platform (Windows/macOS/Linux)

**Paradigms Supported:**
| Paradigm | Description | Example Use |
|---|---|---|
| Procedural | Step-by-step instructions | Scripts, automation |
| OOP | Classes & objects | Web apps, games |
| Functional | Functions as first-class citizens | Data pipelines |

---

## 2. History of Python
| Year | Milestone |
|---|---|
| 1989 | Guido van Rossum began developing Python |
| 1991 | Python 1.0 released |
| 2000 | Python 2.0 (list comprehensions, garbage collection) |
| 2008 | Python 3.0 (major redesign, not backward compatible) |
| 2018 | Guido stepped down as BDFL → steering council formed |
| 2020 | Python 2 officially deprecated |
| Present | Python 3.x is the only maintained version |

> Named after **"Monty Python's Flying Circus"** — not the snake.

---

## 3. Where is Python Used?

**Real-World:**
| Company | Use |
|---|---|
| YouTube | Video streaming, backend |
| Instagram | Scaling infrastructure |
| Spotify | Backend + ML recommendations |
| Netflix | Recommendation engine, CDN |
| Uber | Dynamic pricing, route optimization |

**Domain-Wise:**
| Domain | Key Libraries |
|---|---|
| Web Development | Django, Flask |
| Data Science | Pandas, NumPy, Matplotlib |
| Machine Learning/AI | TensorFlow, PyTorch, Scikit-learn |
| Automation/Scripting | os, shutil, subprocess |
| Cybersecurity | Scapy, Nmap |
| Game Development | Pygame |
| Web Scraping | BeautifulSoup, Scrapy, Selenium |
| Desktop Apps | Tkinter, PyQt |
| Scientific Computing | SciPy, SymPy |
| IoT | MicroPython, Raspberry Pi |
| DevOps/Cloud | Ansible, Boto3 |
| Networking | socket, asyncio |

---

## 4. Python vs Other Languages
| Feature | Python | Java | C++ | JavaScript |
|---|---|---|---|---|
| Syntax | Simple | Verbose | Complex | Moderate |
| Typing | Dynamic | Static | Static | Dynamic |
| Compilation | Interpreted | Compiled | Compiled | Interpreted |
| Speed | Moderate | Fast | Very Fast | Moderate |
| Use Case | Scripting, AI, Web | Enterprise, Android | Systems, Games | Web |
| Learning Curve | Low | Medium | High | Low-Medium |
| Memory Mgmt | Automatic | Automatic | Manual | Automatic |

---

## 5. Hello World
```python
print("Hello, World!")   # Output: Hello, World!
```
- `print()` → built-in function to display text
- Text goes in a **string**, wrapped in `' '` or `" "`

---

## 6. Installing Python

### 6.1 Download & Install
- Get latest Python 3.x from **python.org**
- **Windows:** run `.exe`, ✅ check "Add Python to PATH"
- **macOS:** official `.pkg` installer, or `brew install python3`
- **Linux (Debian/Ubuntu):** `sudo apt-get install python3 python3-pip`

### 6.2 Verify Installation
```bash
python3 --version     # Python 3.12.1
which python3          # location
```

### 6.3 pip — Package Manager
- Comes bundled with Python 3.4+; installs packages from **PyPI**.

```bash
pip install package_name              # install
pip install package_name==1.2.3       # specific version
pip list                              # list installed
pip show package_name                 # details
pip uninstall package_name            # remove
pip install --upgrade package_name    # upgrade
pip install --upgrade pip             # upgrade pip itself
```

**requirements.txt:**
```bash
pip freeze > requirements.txt   # export dependencies
pip install -r requirements.txt # install from file
```

### 6.4 Virtual Environments
- Isolated Python environment per project → avoids dependency conflicts.

```bash
python3 -m venv venv        # create
source venv/bin/activate    # activate (macOS/Linux)
venv\Scripts\activate       # activate (Windows)
deactivate                  # exit venv
```

**Best Practices:**
- One venv per project
- Common names: `venv`, `.venv`, `env`
- Add to `.gitignore` (never commit venv)
- Always use `requirements.txt` to track dependencies

---

## 7. Python IDEs & Editors

| IDE | Best For | Notes |
|---|---|---|
| **VS Code** | General dev, scripting, web | Lightweight, IntelliSense, integrated terminal, Git support |
| **PyCharm** | Large projects, Django/Flask | Community (free) + Professional editions merged; advanced debugging, refactoring |
| **Jupyter Notebook** | Data science, ML, research | Browser-based, run code cell-by-cell, inline plots |

**Jupyter Setup:**
```bash
pip install jupyter
jupyter notebook     # opens at localhost:8888
```
**Shortcuts:** `Shift+Enter` run & next | `Ctrl+Enter` run | `A` insert above | `B` insert below | `DD` delete cell

---

## 📋 Quick Recap
| Topic | Key Point |
|---|---|
| Python | High-level, interpreted, dynamically typed, multi-paradigm |
| History | 1991 (v1.0) → 2008 (v3.0) → Python 2 dead since 2020 |
| Usage | Web, AI/ML, automation, scripting, data science |
| pip | Python's package manager, installs from PyPI |
| venv | Isolated environment per project — always use one |
| IDEs | VS Code (general), PyCharm (big projects), Jupyter (data/ML) |