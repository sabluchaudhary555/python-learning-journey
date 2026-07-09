# Secure Password Analyzer

A command-line Python tool that analyzes password strength based on length, character variety, and predictable personal data, then generates a detailed report with an option to save it to a file.

## Features

- **Interactive Security Scan** — animated progress bar simulating a backend scan using carriage return (`\r`) and `flush=True`
- **Password Strength Scoring** — evaluates password based on:
  - Length (8+ and 12+ character thresholds)
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of numeric digits
- **Personal Data Detection** — flags passwords containing the user's birth year or lucky number, penalizing predictable metadata
- **Safe Input Handling** — uses `try-except` to gracefully handle invalid or missing metadata input
- **Detailed Feedback** — lists specific strengths and weaknesses of the entered password
- **Overall Rating** — classifies the password as `STRONG`, `MODERATE`, or `WEAK`
- **Report Export** — optionally appends the analysis report to `security_report.txt`

## How It Works

1. The user enters a password to analyze.
2. The user enters two numbers (e.g. birth year and a lucky number) used to check for predictable patterns.
3. A simulated scanning animation runs for visual feedback.
4. The password is scored using a simple point-based system:
   - `+2` for 12+ characters
   - `+1` for 8–11 characters
   - `+1` each for uppercase, lowercase, and digit presence
   - `-2` if the password contains the birth year or lucky number
5. A final rating and feedback list are displayed.
6. The user can choose to save the report to a local text file.

## Requirements

- Python 3.6+
- No external libraries — uses only the built-in `time` module

## Usage

```bash
python password_analyzer.py
```

Follow the on-screen prompts to enter a password and optional metadata.

### Example

```
Enter a password to analyze: MyP@ss1990
Enter your birth year and lucky number (separated by space): 1990 7

Initializing Security Scan...
Scanning backend databases: [####################] 100%
Scan Complete!

        --- ANALYSIS RESULTS ---
Password Length: 10
Overall Rating:  MODERATE

Detailed Feedback:
>> Good length (8+ characters)
>> WARNING: Contains predictable personal metadata

Save this report to a text file? (yes/no): yes
Report appended to 'security_report.txt'.
```

## Concepts Practiced

- f-strings and string formatting/padding (`:^40`, `:<20`)
- `try-except` for safe type conversion
- List and string methods (`split()`, `strip()`, `lower()`)
- Character checks with `any()` and generator expressions
- File I/O with `open()` in append mode
- Terminal animation using `\r` and `flush=True`

## Notes

- The password itself is never saved to the report file — only its length, rating, and feedback.
- Running the script multiple times with "yes" will keep appending new reports to `security_report.txt` rather than overwriting it.

