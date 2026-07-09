import time

def check_password_strength():
    print(f"\n{'='*40}")
    print(f"{'SECURE PASSWORD ANALYZER':^40}")
    print(f"{'='*40}\n")

    # 1. Basic Input
    password = input("Enter a password to analyze: ")
    
    # 2. Taking multiple inputs on one line (simulating user metadata)
    user_data = input("Enter your birth year and lucky number (separated by space): ").split()
    
    # 3. Safe type conversion with try-except
    try:
        birth_year = int(user_data[0])
        lucky_num = int(user_data[1])
    except (ValueError, IndexError):
        print("Invalid metadata. Proceeding with basic analysis only.")
        birth_year = 0
        lucky_num = 0

    print("\nInitializing Security Scan...")
    
    # 4. Progress bar using flush=True and carriage return (\r)
    total_steps = 20
    for i in range(total_steps + 1):
        percent = (i / total_steps) * 100
        # The \r returns the cursor to the start of the line, overwriting the previous output
        print(f"\rScanning backend databases: [{('#' * i):<20}] {percent:.0f}%", end="", flush=True)
        time.sleep(0.1)  # Simulating processing time
    
    print("\nScan Complete!\n")

    # 5. Analyzing the password (The Logic)
    score = 0
    feedback = []

    # Check Length
    if len(password) >= 12:
        score += 2
        feedback.append("Excellent length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("Good length (8+ characters)")
    else:
        feedback.append("Password is too short (Under 8 characters)")

    # Check for personal data inclusion (converting numbers to strings for comparison)
    if str(birth_year) in password or str(lucky_num) in password:
        score -= 2
        feedback.append("WARNING: Contains predictable personal metadata")
    
    # Check for character variety (using basic string methods)
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Missing uppercase letters")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Missing lowercase letters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Missing numbers")

    # 6. Formatting Output (f-strings and padding)
    print(f"{'--- ANALYSIS RESULTS ---':^40}")
    print(f"Password Length: {len(password)}")
    
    # Determine overall strength
    if score >= 4:
        status = "STRONG"
    elif score >= 2:
        status = "MODERATE"
    else:
        status = "WEAK"

    print(f"Overall Rating:  {status}")
    
    print("\nDetailed Feedback:")
    # Using sep parameter to format the list output
    for item in feedback:
        print(">>", item, sep=" ")

    # 7. File Output (Saving the report)
    save_option = input("\nSave this report to a text file? (yes/no): ").strip().lower()
    
    if save_option == 'yes':
        try:
            with open("security_report.txt", "a") as file:
                print(f"--- Report for password length {len(password)} ---", file=file)
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