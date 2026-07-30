import re
import os

# simple form validation tool - checks common form fields before they get saved
# useful for signup forms, admin panels, data entry sheets etc.

SAVE_FILE = "valid_entries.txt"


def check_name(name):
    name = name.strip()
    if len(name) < 2:
        return False, "Name too short"
    if not all(c.isalpha() or c == " " for c in name):
        return False, "Name should only have letters and spaces"
    return True, "OK"


def check_username(username):
    username = username.strip()
    if len(username) < 4 or len(username) > 20:
        return False, "Username must be 4-20 characters"
    if not username[0].isalpha():
        return False, "Username must start with a letter"
    if not re.match(r'^[A-Za-z0-9_]+$', username):
        return False, "Only letters, digits and underscore allowed"
    return True, "OK"


def check_email(email):
    email = email.strip()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if re.match(pattern, email):
        return True, "OK"
    return False, "Invalid email format"


def check_phone(phone):
    phone = phone.strip()
    if not phone.isdigit():
        return False, "Phone number should be digits only"
    if len(phone) != 10:
        return False, "Phone number must be exactly 10 digits"
    return True, "OK"


def check_age(age):
    age = age.strip()
    if not age.isdigit():
        return False, "Age must be a number"
    age = int(age)
    if age < 1 or age > 120:
        return False, "Age doesn't look right"
    return True, "OK"


def check_password(password):
    if len(password) < 8:
        return False, "Password should be at least 8 characters"
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=" for c in password)
    if not (has_upper and has_digit and has_special):
        return False, "Password needs an uppercase letter, a digit and a special char"
    return True, "OK"


def ask_until_valid(field_name, check_func, hide_input=False):
    while True:
        value = input(f"Enter {field_name}: ")
        ok, msg = check_func(value)
        if ok:
            print(f"  -> {field_name} looks good")
            return value
        print(f"  -> {msg}, try again")


def fill_form():
    print("\n--- New Form Entry ---")
    name = ask_until_valid("full name", check_name)
    username = ask_until_valid("username", check_username)
    email = ask_until_valid("email", check_email)
    phone = ask_until_valid("phone number", check_phone)
    age = ask_until_valid("age", check_age)
    password = ask_until_valid("password", check_password)

    entry = f"{name} | {username} | {email} | {phone} | {age} | {'*' * len(password)}"

    with open(SAVE_FILE, "a") as f:
        f.write(entry + "\n")

    print("\nForm saved successfully!")


def check_single_field():
    print("\nWhich field do you want to check?")
    print("1. Name  2. Username  3. Email  4. Phone  5. Age  6. Password")
    choice = input("Choice: ").strip()

    fields = {
        "1": ("name", check_name),
        "2": ("username", check_username),
        "3": ("email", check_email),
        "4": ("phone number", check_phone),
        "5": ("age", check_age),
        "6": ("password", check_password),
    }

    if choice not in fields:
        print("Not a valid option")
        return

    label, func = fields[choice]
    value = input(f"Enter {label}: ")
    ok, msg = func(value)
    print("Valid!" if ok else f"Invalid - {msg}")


def view_saved_entries():
    if not os.path.exists(SAVE_FILE):
        print("No entries saved yet.")
        return
    print("\n--- Saved Entries ---")
    with open(SAVE_FILE) as f:
        lines = f.readlines()
    if not lines:
        print("File is empty.")
        return
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")


def clear_entries():
    confirm = input("This will delete all saved entries. Type 'yes' to confirm: ")
    if confirm.lower() == "yes":
        open(SAVE_FILE, "w").close()
        print("All entries cleared.")
    else:
        print("Cancelled.")


def menu():
    print("\n===== Smart Form Input Checker =====")
    print("1. Fill a new form")
    print("2. Check a single field")
    print("3. View saved entries")
    print("4. Clear all entries")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            fill_form()
        elif choice == "2":
            check_single_field()
        elif choice == "3":
            view_saved_entries()
        elif choice == "4":
            clear_entries()
        elif choice == "0":
            print("bye!")
            break
        else:
            print("invalid option")


if __name__ == "__main__":
    main()