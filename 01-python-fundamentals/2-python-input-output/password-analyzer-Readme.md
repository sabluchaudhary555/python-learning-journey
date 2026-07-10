# Secure Password Analyzer

A command-line Python tool that analyzes password strength by estimating how long it would take to crack, converts that into a strength percentage, and lets you check as many passwords as you want in one run.

## Features

- **Interactive Security Scan** — animated progress bar simulating a backend scan using carriage return (`\r`) and `flush=True`
- **Crack-Time Based Scoring** — estimates strength using the actual character pool used in the password (lowercase, uppercase, digits, symbols) and calculates how long it would take to brute-force
- **Strength Percentage** — converts the estimated crack time into a 0–100% score using a logarithmic scale, since crack times range from seconds to billions of years
- **Overall Rating** — classifies the password as `STRONG`, `MODERATE`, or `WEAK`
- **Detailed Feedback** — flags missing character types (uppercase, lowercase, numbers, symbols) and length issues
- **Report Export** — optionally appends the analysis report to `security_report.txt`
- **Repeat Checks** — after each analysis, choose to check another password or exit the program

## How It Works

1. Enter a password to analyze.
2. A simulated scanning animation runs for visual feedback.
3. The tool detects which character types are present and calculates the total possible combinations for that password's length and character pool.
4. Assuming an attacker can attempt 10 billion guesses per second, it estimates the time to crack the password.
5. That crack time is converted into a strength percentage (0–100%) and an overall rating.
6. Feedback is shown for any missing character types or length issues.
7. You can save the report to a local text file.
8. You're asked whether to check another password or exit.

## Strength Scale

| Strength Score | Rating   |
|-----------------|----------|
| 80–100%         | STRONG   |
| 40–79%          | MODERATE |
| 0–39%           | WEAK     |

## Requirements

- Python 3.6+
- No external libraries — uses only the built-in `time` and `math` modules

## Usage

```bash
python password_analyzer.py
```

Follow the on-screen prompts to enter a password.

### Example

```
Enter a password to analyze: Tr@ilBlazer92

Initializing Security Scan...
Scanning backend databases: [####################] 100%
Scan Complete!

        --- ANALYSIS RESULTS ---
Password Length:      13
Estimated Crack Time: 200,000 years
Strength Score:       92%
Overall Rating:       STRONG

Detailed Feedback:
>> Excellent length (12+ characters)

Save this report to a text file? (yes/no): yes
Report appended to 'security_report.txt'.

Check another password? (yes/no): no

Exiting Secure Password Analyzer. Stay safe!
```

## Concepts Practiced

- f-strings and string formatting/padding (`:^40`, `:<20`, `:,`)
- Character pool detection using `any()` with generator expressions
- Brute-force combination math (`pool_size ** length`)
- Logarithmic scaling with the `math` module
- File I/O with `open()` in append mode
- Terminal animation using `\r` and `flush=True`
- Program looping with `while True` and a break condition

## Notes

- The password itself is never saved to the report file — only its length, crack time estimate, strength score, and feedback.
- Crack time is an estimate based on brute-force guessing at 10 billion guesses/second; real-world numbers vary depending on the hashing algorithm and attack method used.
- Running the script multiple times with "yes" keeps appending new reports to `security_report.txt` rather than overwriting it.

