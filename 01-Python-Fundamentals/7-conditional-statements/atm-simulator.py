import os
from datetime import date

# simple ATM withdrawal simulator - checks pin, balance, daily limit
# and breaks down the amount into notes like a real ATM would

# file to store account balance persistently
ACCOUNT_FILE = "account.txt"
# file to log all withdrawal transactions with date
LOG_FILE = "transactions.txt"

# ATM business rules - all limits in rupees
DAILY_LIMIT = 25000       # max total withdrawal allowed per day
MIN_WITHDRAW = 100        # smallest amount ATM will dispense
MAX_PER_TXN = 10000       # max single transaction limit
CORRECT_PIN = "4321"      # hardcoded PIN for simulation


def load_balance():
    # if account file doesn't exist yet, create it with default balance of 50000
    if not os.path.exists(ACCOUNT_FILE):
        # first time setup
        with open(ACCOUNT_FILE, "w") as f:
            f.write("50000")
        return 50000
    # read existing balance from file and return as integer
    with open(ACCOUNT_FILE) as f:
        return int(f.read().strip())


def save_balance(balance):
    # overwrite the account file with the updated balance after each transaction
    with open(ACCOUNT_FILE, "w") as f:
        f.write(str(balance))


def get_today_withdrawn():
    # if no transaction log exists yet, nothing has been withdrawn today
    if not os.path.exists(LOG_FILE):
        return 0
    today = str(date.today())  # get current date as string e.g. "2026-08-10"
    total = 0
    # scan log file and sum up all withdrawals that happened today
    with open(LOG_FILE) as f:
        for line in f:
            parts = line.strip().split(",")  # each line format: "date,amount"
            if len(parts) == 2 and parts[0] == today:
                total += int(parts[1])  # add this transaction's amount to total
    return total


def log_transaction(amount):
    # append today's date and withdrawn amount to the log file
    today = str(date.today())
    with open(LOG_FILE, "a") as f:  # "a" mode appends without erasing old logs
        f.write(f"{today},{amount}\n")


def check_pin():
    tries = 3  # user gets 3 attempts before being locked out
    while tries > 0:
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            return True  # PIN matched - grant access
        tries -= 1
        print(f"Wrong PIN. {tries} attempt(s) left.")
    return False  # all 3 attempts exhausted - deny access


def breakdown_notes(amount):
    # figures out how many 500s, 200s, 100s to give out
    notes = [500, 200, 100]  # denomination list in descending order (greedy approach)
    result = {}              # stores {denomination: count} pairs
    remaining = amount       # tracks how much is still left to dispense

    for note in notes:
        count = remaining // note   # how many of this note fit into remaining amount
        if count > 0:
            result[note] = count            # store count for this denomination
            remaining -= note * count       # subtract dispensed amount from remaining

    return result, remaining  # remaining > 0 means amount can't be fully dispensed


def withdraw_cash():
    balance = load_balance()                    # fetch current account balance
    already_withdrawn = get_today_withdrawn()   # fetch total withdrawn so far today

    amount_str = input("Enter amount to withdraw: Rs. ")
    # reject non-numeric input immediately
    if not amount_str.isdigit():
        print("Enter a valid number.")
        return

    amount = int(amount_str)

    # check 1 - minimum withdrawal limit
    if amount < MIN_WITHDRAW:
        print(f"Minimum withdrawal amount is Rs. {MIN_WITHDRAW}")
        return

    # check 2 - amount must be in multiples of 100 (ATM note constraint)
    if amount % 100 != 0:
        print("Amount must be in multiples of 100.")
        return

    # check 3 - single transaction limit
    if amount > MAX_PER_TXN:
        print(f"You can't withdraw more than Rs. {MAX_PER_TXN} in a single transaction.")
        return

    # check 4 - sufficient account balance
    if amount > balance:
        print(f"Insufficient balance. Your current balance is Rs. {balance}")
        return

    # check 5 - daily withdrawal limit
    if already_withdrawn + amount > DAILY_LIMIT:
        remaining_limit = DAILY_LIMIT - already_withdrawn
        if remaining_limit <= 0:
            print("You've already hit your daily withdrawal limit.")
        else:
            print(f"This exceeds your daily limit. You can only withdraw Rs. {remaining_limit} more today.")
        return

    # calculate note breakdown for the requested amount
    notes, leftover = breakdown_notes(amount)

    # check 6 - ATM can only dispense in 100/200/500 notes
    if leftover > 0:
        print("ATM can't dispense this exact amount with available denominations, try a different amount.")
        return

    # all checks passed, go ahead
    balance -= amount       # deduct withdrawn amount from balance
    save_balance(balance)   # persist updated balance to file
    log_transaction(amount) # record this transaction in log

    # display note-wise cash breakdown to user
    print("\nPlease collect your cash:")
    for note, count in notes.items():
        print(f"  {count} x Rs.{note} note{'s' if count > 1 else ''}")

    print(f"\nWithdrawal successful. Remaining balance: Rs. {balance}")


def check_balance():
    # load and display current account balance
    balance = load_balance()
    print(f"Your current balance is Rs. {balance}")


def deposit_cash():
    amount_str = input("Enter amount to deposit: Rs. ")
    # validate input - must be a positive number
    if not amount_str.isdigit() or int(amount_str) <= 0:
        print("Enter a valid amount.")
        return

    amount = int(amount_str)
    balance = load_balance()    # get current balance
    balance += amount           # add deposit amount to balance
    save_balance(balance)       # save updated balance to file
    print(f"Deposited Rs. {amount}. New balance: Rs. {balance}")


def view_today_transactions():
    today = str(date.today())
    # if log file doesn't exist, no transactions have been made
    if not os.path.exists(LOG_FILE):
        print("No transactions yet.")
        return

    found = False   # flag to track if any transactions found for today
    total = 0       # accumulator for total amount withdrawn today
    print(f"\nTransactions for {today}:")
    with open(LOG_FILE) as f:
        for line in f:
            parts = line.strip().split(",")   # split "date,amount" into list
            if len(parts) == 2 and parts[0] == today:
                print(f"  Withdrew Rs. {parts[1]}")
                total += int(parts[1])   # add to running total
                found = True

    # show summary or empty state
    if not found:
        print("  No withdrawals today.")
    else:
        print(f"Total withdrawn today: Rs. {total} / Rs. {DAILY_LIMIT}")


def menu():
    # display main ATM menu options
    print("\n===== ATM Machine =====")
    print("1. Withdraw Cash")
    print("2. Check Balance")
    print("3. Deposit Cash")
    print("4. Today's Transactions")
    print("0. Exit")


def main():
    print("Welcome to Quick ATM")

    # verify PIN before allowing any operations
    if not check_pin():
        print("Too many wrong attempts. Card blocked, try again later.")
        return

    # main loop - keeps running until user chooses to exit
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


# entry point - only runs main() when script is executed directly
# not when imported as a module
if __name__ == "__main__":
    main()