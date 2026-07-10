import time
import math

def estimate_crack_time_seconds(password):
    # Figure out which character sets are being used
    pool_size = 0
    if any(char.islower() for char in password):
        pool_size += 26
    if any(char.isupper() for char in password):
        pool_size += 26
    if any(char.isdigit() for char in password):
        pool_size += 10
    if any(not char.isalnum() for char in password):
        pool_size += 32  # common symbols

    if pool_size == 0:
        return 0

    # Total possible combinations for this password length and pool size
    total_combinations = pool_size ** len(password)

    # Assume an attacker can try 10 billion guesses per second (offline attack)
    guesses_per_second = 10_000_000_000

    # On average, the password is found halfway through the search space
    crack_time = total_combinations / guesses_per_second / 2
    return crack_time


def format_crack_time(seconds):
    if seconds < 1:
        return "Instantly"
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365

    if seconds < minute:
        return f"{seconds:.0f} seconds"
    elif seconds < hour:
        return f"{seconds/minute:.0f} minutes"
    elif seconds < day:
        return f"{seconds/hour:.0f} hours"
    elif seconds < year:
        return f"{seconds/day:.0f} days"
    else:
        return f"{seconds/year:,.0f} years"


def crack_time_to_percent(seconds):
    if seconds < 1:
        return 0

    # 10 billion years is treated as "basically uncrackable" -> 100%
    max_seconds = 10_000_000_000 * 365 * 24 * 60 * 60

    percent = (math.log10(seconds) / math.log10(max_seconds)) * 100
    percent = max(0, min(100, percent))
    return round(percent)


def check_password_strength():
    print(f"\n{'='*40}")
    print(f"{'SECURE PASSWORD ANALYZER':^40}")
    print(f"{'='*40}\n")

    # 1. Basic Input
    password = input("Enter a password to analyze: ")

    print("\nInitializing Security Scan...")

    # 2. Progress bar using flush=True and carriage return (\r)
    total_steps = 20
    for i in range(total_steps + 1):
        percent = (i / total_steps) * 100
        # The \r returns the cursor to the start of the line, overwriting the previous output
        print(f"\rScanning backend databases: [{('#' * i):<20}] {percent:.0f}%", end="", flush=True)
        time.sleep(0.1)  # Simulating processing time

    print("\nScan Complete!\n")

    # 3. Estimate crack time and convert to a strength percentage
    crack_seconds = estimate_crack_time_seconds(password)
    crack_time_readable = format_crack_time(crack_seconds)
    strength_percent = crack_time_to_percent(crack_seconds)

    feedback = []

    # Length feedback
    if len(password) >= 12:
        feedback.append("Excellent length (12+ characters)")
    elif len(password) >= 8:
        feedback.append("Good length (8+ characters)")
    else:
        feedback.append("Password is too short (Under 8 characters)")

    # Character variety feedback
    if any(char.isupper() for char in password):
        pass
    else:
        feedback.append("Missing uppercase letters")

    if any(char.islower() for char in password):
        pass
    else:
        feedback.append("Missing lowercase letters")

    if any(char.isdigit() for char in password):
        pass
    else:
        feedback.append("Missing numbers")

    if any(not char.isalnum() for char in password):
        pass
    else:
        feedback.append("Missing special symbols")

    # 4. Determine overall rating from the percentage
    if strength_percent >= 80:
        status = "STRONG"
    elif strength_percent >= 40:
        status = "MODERATE"
    else:
        status = "WEAK"

    # 5. Formatting Output (f-strings and padding)
    print(f"{'--- ANALYSIS RESULTS ---':^40}")
    print(f"Password Length:      {len(password)}")
    print(f"Estimated Crack Time: {crack_time_readable}")
    print(f"Strength Score:       {strength_percent}%")
    print(f"Overall Rating:       {status}")

    print("\nDetailed Feedback:")
    for item in feedback:
        print(">>", item, sep=" ")

    # 6. File Output (Saving the report)
    save_option = input("\nSave this report to a text file? (yes/no): ").strip().lower()

    if save_option == 'yes':
        try:
            with open("security_report.txt", "a") as file:
                print(f"--- Report for password length {len(password)} ---", file=file)
                print(f"Estimated Crack Time: {crack_time_readable}", file=file)
                print(f"Strength Score: {strength_percent}%", file=file)
                print(f"Rating: {status}", file=file)
                for item in feedback:
                    print(f"- {item}", file=file)
                print("="*30, file=file)
            print("Report appended to 'security_report.txt'.")
        except Exception as e:
            print(f"Error saving file: {e}")

# Run the program
if __name__ == "__main__":
    check_password_strength()