# 📋 Attendance Register System

A menu-driven Python CLI project built to practice and demonstrate **Python Data Types** — `str`, `list`, `tuple`, `dict`, `bool`, `set`, `frozenset`, and `bytes` — through a real-world use case.

---

## 📌 Overview

This project simulates a classroom attendance register where you can add students, mark daily attendance, calculate attendance percentage, detect defaulters, and export/save data — all while using core Python data structures purposefully.

**Class Info:** `("Class 10", "Section A", 2026)` — stored as a **tuple** since it shouldn't change during runtime.

---

## ✨ Features

| # | Feature | Data Type Used |
|---|---|---|
| 1 | Add / Remove students | `dict` |
| 2 | Mark attendance (present/absent) | `set` |
| 3 | View attendance for a date | `dict` + `set` |
| 4 | Attendance % of a student | numeric + `bool` logic |
| 5 | List defaulters (<75%) | list comprehension |
| 6 | Search student by roll number | `dict.get()` |
| 7 | Holiday check | `frozenset` |
| 8 | Fixed class info | `tuple` |
| 9 | Export attendance as binary log | `bytes` / `bytearray` |
| 10 | Save / Load register | file handling |
| 11 | Undo last marked attendance | `list` (stack-like) |
| 12 | Show full register | dict/set iteration |

---

## 🛠️ How It Works

- **Students** are stored in a `dict` → `{roll_no: name}`
- **Attendance** is stored as `{date: set(roll numbers present)}` — a `set` prevents duplicate entries for the same student on the same day
- **Holidays** are stored in a `frozenset` for fast, immutable lookup — attendance can't be marked on a holiday
- **Undo** uses a `list` as a simple stack — pop the last marked action to reverse it
- **Binary export** converts attendance records into `bytes` and writes them to `attendance_log.bin`
- **Save/Load** persists the student register to a plain text file (`register.txt`)

---

## 🚀 Usage

```bash
python attendance_register.py
```

You'll see a menu like this:

```
===== Attendance Register (Class 10 - Section A, 2026) =====
1. Add Student
2. Remove Student
3. Mark Attendance
4. Undo Last Attendance
5. View Attendance (by date)
6. Check Attendance % of a Student
7. List Defaulters (<75%)
8. Search Student
9. Export Attendance as Binary Log
10. Save Register to File
11. Load Register from File
0. Exit
```

Just enter the number of the action you want and follow the prompts.

---

## 📂 Files Generated

| File | Description |
|---|---|
| `register.txt` | Saved student list (roll number + name) |
| `attendance_log.bin` | Binary export of attendance records |

---

## 📖 Example Flow

1. Add a few students (roll number + name)
2. Mark attendance for a date (skips automatically if it's a holiday)
3. View attendance for that date
4. Check a student's attendance percentage
5. List defaulters below 75%
6. Export everything to a binary log or save the register to file

---

## 🧠 What I Learned

This project was built while practicing **Python Data Types** — specifically how to choose the *right* data structure for the *right* job:
- `set` for uniqueness and fast membership checks
- `frozenset` for immutable, unchanging reference data
- `tuple` for fixed, read-only info
- `dict` for key-based lookups
- `bytes`/`bytearray` for binary data handling

---

