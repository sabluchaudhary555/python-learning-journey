import os
from datetime import date

# simple ATM withdrawal simulator - checks pin, balance, daily limit
# and breaks down the amount into notes like a real ATM would

ACCOUNT_FILE = "account.txt"
LOG_FILE = "transactions.txt"

DAILY_LIMIT = 25000
MIN_WITHDRAW = 100
MAX_PER_TXN = 10000
CORRECT_PIN = "4321"


def load_balance():
    if not os.path.exists(ACCOUNT_FILE):
        # first time setup
        with open(ACCOUNT_FILE, "w") as f:
            f.write("50000")
        return 50000
    with open(ACCOUNT_FILE) as f:
        return int(f.read().strip())


def save_balance(balance):
    with open(ACCOUNT_FILE, "w") as f:
        f.write(str(balance))


def get_today_withdrawn():
    if not os.path.exists(LOG_FILE):
        return 0
    today = str(date.today())
    total = 0
    with open(LOG_FILE) as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2 and parts[0] == today:
                total += int(parts[1])
    return total


def log_transaction(amount):
    today = str(date.today())
    with open(LOG_FILE, "a") as f:
        f.write(f"{today},{amount}\n")


def check_pin():
    tries = 3
    while tries > 0:
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            return True
        tries -= 1
        print(f"Wrong PIN. {tries} attempt(s) left.")
    return False


def breakdown_notes(amount):
    # figures out how many 500s, 200s, 100s to give out
    notes = [500, 200, 100]
    result = {}
    remaining = amount

    for note in notes:
        count = remaining // note
        if count > 0:
            result[note] = count
            remaining -= note * count

    return result, remaining


def withdraw_cash():
    balance = load_balance()
    already_withdrawn = get_today_withdrawn()

    amount_str = input("Enter amount to withdraw: Rs. ")
    if not amount_str.isdigit():
        print("Enter a valid number.")
        return

    amount = int(amount_str)

    if amount < MIN_WITHDRAW:
        print(f"Minimum withdrawal amount is Rs. {MIN_WITHDRAW}")
        return

    if amount % 100 != 0:
        print("Amount must be in multiples of 100.")
        return

    if amount > MAX_PER_TXN:
        print(f"You can't withdraw more than Rs. {MAX_PER_TXN} in a single transaction.")
        return

    if amount > balance:
        print(f"Insufficient balance. Your current balance is Rs. {balance}")
        return

    if already_withdrawn + amount > DAILY_LIMIT:
        remaining_limit = DAILY_LIMIT - already_withdrawn
        if remaining_limit <= 0:
            print("You've already hit your daily withdrawal limit.")
        else:
            print(f"This exceeds your daily limit. You can only withdraw Rs. {remaining_limit} more today.")
        return

    notes, leftover = breakdown_notes(amount)

    if leftover > 0:
        print("ATM can't dispense this exact amount with available denominations, try a different amount.")
        return

    # all checks passed, go ahead
    balance -= amount
    save_balance(balance)
    log_transaction(amount)

    print("\nPlease collect your cash:")
    for note, count in notes.items():
        print(f"  {count} x Rs.{note} note{'s' if count > 1 else ''}")

    print(f"\nWithdrawal successful. Remaining balance: Rs. {balance}")


def check_balance():
    balance = load_balance()
    print(f"Your current balance is Rs. {balance}")


def deposit_cash():
    amount_str = input("Enter amount to deposit: Rs. ")
    if not amount_str.isdigit() or int(amount_str) <= 0:
        print("Enter a valid amount.")
        return

    amount = int(amount_str)
    balance = load_balance()
    balance += amount
    save_balance(balance)
    print(f"Deposited Rs. {amount}. New balance: Rs. {balance}")


def view_today_transactions():
    today = str(date.today())
    if not os.path.exists(LOG_FILE):
        print("No transactions yet.")
        return

    found = False
    total = 0
    print(f"\nTransactions for {today}:")
    with open(LOG_FILE) as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2 and parts[0] == today:
                print(f"  Withdrew Rs. {parts[1]}")
                total += int(parts[1])
                found = True

    if not found:
        print("  No withdrawals today.")
    else:
        print(f"Total withdrawn today: Rs. {total} / Rs. {DAILY_LIMIT}")


def menu():
    print("\n===== ATM Machine =====")
    print("1. Withdraw Cash")
    print("2. Check Balance")
    print("3. Deposit Cash")
    print("4. Today's Transactions")
    print("0. Exit")


def main():
    print("Welcome to Quick ATM")

    if not check_pin():
        print("Too many wrong attempts. Card blocked, try again later.")
        return

    while True:
        menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            withdraw_cash()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            deposit_cash()
        elif choice == "4":
            view_today_transactions()
        elif choice == "0":
            print("Thank you, have a nice day!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()