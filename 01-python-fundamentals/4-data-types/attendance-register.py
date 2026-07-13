"""
Attendance Register System
---------------------------
A mini project built to practice Python Data Types:
int, float, str, list, tuple, dict, bool, set, frozenset, bytes

Features:
1. Add / Remove students          -> dict
2. Mark attendance (present/absent)-> set (per date)
3. View attendance for a date      -> dict + set
4. Attendance % of a student       -> numeric + bool logic
5. List defaulters (<75%)          -> list comprehension
6. Search student by roll no       -> dict lookup
7. Holiday check                   -> frozenset (immutable list of holidays)
8. Class info (fixed, can't change)-> tuple
9. Save attendance log as binary   -> bytes / bytearray
10. Load / Save data to a text file-> file handling
11. Undo last marked attendance    -> list (stack-like use)
12. Show full register             -> loop over dict/set
"""

import os

# ---------- Fixed class info (tuple = immutable) ----------
CLASS_INFO = ("Class 10", "Section A", 2026)   # (class, section, year)

# ---------- Holidays (frozenset = immutable, fast lookup) ----------
HOLIDAYS = frozenset(["2026-01-26", "2026-08-15", "2026-10-02"])

# ---------- Core data structures ----------
students = {}          # dict -> {roll_no: name}
attendance = {}         # dict -> {date: set(roll numbers present)}
undo_stack = []          # list -> stores last actions for undo


def add_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("Roll number already exists.")
        return
    name = input("Enter student name: ").strip()
    students[roll] = name
    print(f"Added: {roll} -> {name}")


def remove_student():
    roll = input("Enter roll number to remove: ").strip()
    if roll not in students:
        print("Student not found.")
        return
    removed_name = students.pop(roll)
    # also clean up from all attendance records
    for date in attendance:
        attendance[date].discard(roll)
    print(f"Removed {removed_name} (Roll {roll}) from register.")


def is_holiday(date):
    # bool check using frozenset membership
    return date in HOLIDAYS


def mark_attendance():
    date = input("Enter date (YYYY-MM-DD): ").strip()

    if is_holiday(date):
        print(f"{date} is a holiday. Attendance not marked.")
        return

    if not students:
        print("No students in register yet.")
        return

    if date not in attendance:
        attendance[date] = set()      # set avoids duplicate roll entries

    print("Enter roll numbers of PRESENT students, comma separated:")
    entered = input("> ").strip()
    present_rolls = {r.strip() for r in entered.split(",") if r.strip()}

    valid_rolls = present_rolls & students.keys()   # set intersection
    invalid_rolls = present_rolls - students.keys()

    attendance[date].update(valid_rolls)
    undo_stack.append((date, valid_rolls))    # save for undo

    print(f"Marked {len(valid_rolls)} student(s) present on {date}.")
    if invalid_rolls:
        print(f"Skipped invalid roll numbers: {invalid_rolls}")


def undo_last_mark():
    if not undo_stack:
        print("Nothing to undo.")
        return
    date, rolls = undo_stack.pop()
    attendance[date] -= rolls          # set difference removes them
    print(f"Undo successful: removed {rolls} from {date}'s attendance.")


def view_attendance(date):
    if date not in attendance:
        print("No attendance record for this date.")
        return

    present = attendance[date]
    print(f"\nAttendance for {date}  ({CLASS_INFO[0]} - {CLASS_INFO[1]})")
    print("-" * 40)
    for roll, name in students.items():
        status = "Present" if roll in present else "Absent"   # bool-driven
        print(f"{roll:<8} {name:<15} {status}")
    print("-" * 40)
    print(f"Total Present: {len(present)} / {len(students)}\n")


def attendance_percentage(roll):
    if roll not in students:
        print("Student not found.")
        return None

    total_days = len(attendance)
    if total_days == 0:
        print("No attendance data yet.")
        return None

    days_present = sum(1 for date in attendance if roll in attendance[date])
    percent = (days_present / total_days) * 100
    print(f"{students[roll]} (Roll {roll}) -> {percent:.2f}% attendance")
    return percent


def list_defaulters(threshold=75.0):
    print(f"\nDefaulters (attendance below {threshold}%):")
    print("-" * 40)
    found = False
    for roll in students:
        total_days = len(attendance)
        if total_days == 0:
            continue
        days_present = sum(1 for date in attendance if roll in attendance[date])
        percent = (days_present / total_days) * 100
        if percent < threshold:
            print(f"{roll:<8} {students[roll]:<15} {percent:.2f}%")
            found = True
    if not found:
        print("No defaulters found (or no data yet).")
    print("-" * 40)


def search_student():
    roll = input("Enter roll number to search: ").strip()
    name = students.get(roll)          # dict .get() avoids KeyError
    if name:
        print(f"Found: {roll} -> {name}")
    else:
        print("Student not found.")


def export_binary_log():
    # demonstrates bytes / bytearray usage
    log_lines = bytearray()
    for date, rolls in attendance.items():
        line = f"{date}: {sorted(rolls)}\n"
        log_lines += line.encode("utf-8")     # str -> bytes

    with open("attendance_log.bin", "wb") as f:
        f.write(bytes(log_lines))             # bytearray -> bytes

    print(f"Binary log exported ({len(log_lines)} bytes) -> attendance_log.bin")


def save_register(filename="register.txt"):
    with open(filename, "w") as f:
        for roll, name in students.items():
            f.write(f"{roll},{name}\n")
    print(f"Register saved to {filename}")


def load_register(filename="register.txt"):
    if not os.path.exists(filename):
        print("No saved register found.")
        return
    with open(filename, "r") as f:
        for line in f:
            roll, name = line.strip().split(",", 1)
            students[roll] = name
    print(f"Register loaded from {filename}")


def show_menu():
    print(f"\n===== Attendance Register ({CLASS_INFO[0]} - {CLASS_INFO[1]}, {CLASS_INFO[2]}) =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Mark Attendance")
    print("4. Undo Last Attendance")
    print("5. View Attendance (by date)")
    print("6. Check Attendance % of a Student")
    print("7. List Defaulters (<75%)")
    print("8. Search Student")
    print("9. Export Attendance as Binary Log")
    print("10. Save Register to File")
    print("11. Load Register from File")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            undo_last_mark()
        elif choice == "5":
            date = input("Enter date to view (YYYY-MM-DD): ").strip()
            view_attendance(date)
        elif choice == "6":
            roll = input("Enter roll number: ").strip()
            attendance_percentage(roll)
        elif choice == "7":
            list_defaulters()
        elif choice == "8":
            search_student()
        elif choice == "9":
            export_binary_log()
        elif choice == "10":
            save_register()
        elif choice == "11":
            load_register()
        elif choice == "0":
            print("Exiting... Attendance saved in memory only unless exported.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()