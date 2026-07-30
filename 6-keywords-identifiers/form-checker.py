import re
import os
import csv
import random
import hashlib

# Smart Form Input Checker - now works more like an actual signup system
# validates fields, blocks duplicate accounts, hashes passwords, verifies email with OTP,
# lets you search/edit/delete records - basically a mini user registration system

SAVE_FILE = "users.csv"
FIELDS = ["user_id", "name", "username", "email", "phone", "age", "password_hash"]


# ---------- validation rules ----------

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


def ask_until_valid(field_name, check_func):
    while True:
        value = input(f"Enter {field_name}: ")
        ok, msg = check_func(value)
        if ok:
            print(f"  -> {field_name} looks good")
            return value
        print(f"  -> {msg}, try again")


# ---------- storage helpers ----------

def load_users():
    if not os.path.exists(SAVE_FILE):
        return []
    with open(SAVE_FILE, newline="") as f:
        return list(csv.DictReader(f))


def save_all_users(users):
    with open(SAVE_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(users)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_user_id(users):
    if not users:
        return "U1001"
    last_id = max(int(u["user_id"][1:]) for u in users)
    return f"U{last_id + 1}"


def username_taken(username, users):
    return any(u["username"].lower() == username.lower() for u in users)


def email_taken(email, users):
    return any(u["email"].lower() == email.lower() for u in users)


# ---------- OTP simulation ----------

def verify_email_otp(email):
    otp = str(random.randint(100000, 999999))
    print(f"\n(simulated) OTP sent to {email}: {otp}")
    attempts = 3
    while attempts > 0:
        entered = input("Enter the OTP to verify your email: ").strip()
        if entered == otp:
            print("Email verified!")
            return True
        attempts -= 1
        print(f"Wrong OTP, {attempts} attempt(s) left")
    print("Too many failed attempts, verification failed.")
    return False


# ---------- core actions ----------

def sign_up():
    print("\n--- New Account Signup ---")
    users = load_users()

    while True:
        name = ask_until_valid("full name", check_name)
        username = ask_until_valid("username", check_username)
        if username_taken(username, users):
            print("  -> That username is already taken, pick another")
            continue
        break

    while True:
        email = ask_until_valid("email", check_email)
        if email_taken(email, users):
            print("  -> An account with this email already exists")
            continue
        break

    phone = ask_until_valid("phone number", check_phone)
    age = ask_until_valid("age", check_age)
    password = ask_until_valid("password", check_password)

    if not verify_email_otp(email):
        print("Signup cancelled - email not verified.")
        return

    new_user = {
        "user_id": generate_user_id(users),
        "name": name,
        "username": username,
        "email": email,
        "phone": phone,
        "age": age,
        "password_hash": hash_password(password),
    }

    users.append(new_user)
    save_all_users(users)
    print(f"\nAccount created! Your user ID is {new_user['user_id']}")


def log_in():
    print("\n--- Login ---")
    users = load_users()
    username = input("Username: ").strip()
    password = input("Password: ")

    match = next((u for u in users if u["username"].lower() == username.lower()), None)
    if not match:
        print("No account found with that username.")
        return

    if match["password_hash"] == hash_password(password):
        print(f"Welcome back, {match['name']}!")
    else:
        print("Wrong password.")


def search_user():
    users = load_users()
    term = input("Search by username or email: ").strip().lower()
    results = [u for u in users if term in u["username"].lower() or term in u["email"].lower()]

    if not results:
        print("No matching users.")
        return

    for u in results:
        print(f"{u['user_id']} | {u['name']} | {u['username']} | {u['email']} | {u['phone']} | age {u['age']}")


def edit_user():
    users = load_users()
    user_id = input("Enter user ID to edit: ").strip()
    match = next((u for u in users if u["user_id"] == user_id), None)

    if not match:
        print("User not found.")
        return

    print("Leave blank to keep the current value.")
    new_phone = input(f"Phone [{match['phone']}]: ").strip()
    if new_phone:
        ok, msg = check_phone(new_phone)
        if ok:
            match["phone"] = new_phone
        else:
            print(f"  -> {msg}, phone not updated")

    new_email = input(f"Email [{match['email']}]: ").strip()
    if new_email:
        ok, msg = check_email(new_email)
        if ok and not email_taken(new_email, [u for u in users if u["user_id"] != user_id]):
            match["email"] = new_email
        else:
            print("  -> couldn't update email (invalid or already taken)")

    save_all_users(users)
    print("Profile updated.")


def delete_user():
    users = load_users()
    user_id = input("Enter user ID to delete: ").strip()
    match = next((u for u in users if u["user_id"] == user_id), None)

    if not match:
        print("User not found.")
        return

    confirm = input(f"Delete account for {match['name']} ({match['username']})? Type 'yes' to confirm: ")
    if confirm.lower() == "yes":
        users.remove(match)
        save_all_users(users)
        print("Account deleted.")
    else:
        print("Cancelled.")


def view_all_users():
    users = load_users()
    if not users:
        print("No registered users yet.")
        return
    print(f"\nTotal registered users: {len(users)}")
    for u in users:
        print(f"{u['user_id']} | {u['name']} | {u['username']} | {u['email']} | {u['phone']} | age {u['age']}")


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


def menu():
    print("\n===== Smart Form Input Checker - Mini Registration System =====")
    print("1. Sign up (create account)")
    print("2. Log in")
    print("3. Search user")
    print("4. Edit profile")
    print("5. Delete account")
    print("6. View all registered users")
    print("7. Just check a single field (no saving)")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        elif choice == "3":
            search_user()
        elif choice == "4":
            edit_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            view_all_users()
        elif choice == "7":
            check_single_field()
        elif choice == "0":
            print("bye!")
            break
        else:
            print("invalid option")


if __name__ == "__main__":
    main()