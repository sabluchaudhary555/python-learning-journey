# Smart Form Input Checker — Mini Registration System

A CLI tool that works like an actual signup/login system, not just a field validator. It checks form inputs, blocks duplicate accounts, hashes passwords, verifies email with a simulated OTP, and lets you manage user records — the same core logic real apps use for registration.

## Why this exists

Field validation alone (checking if an email "looks right") isn't how real systems work. Real signup flows also check for duplicates, confirm your email, never store your password as plain text, and let you manage your account afterward. This project recreates that full flow in a small CLI tool.

## Features

| Feature | What it does |
|---|---|
| Sign up | Validates every field, blocks duplicate username/email, verifies email with a mock OTP, hashes the password, generates a unique user ID |
| Log in | Checks username + password against stored (hashed) credentials |
| Search user | Find an account by partial username or email |
| Edit profile | Update phone/email for an existing user ID (re-validates before saving) |
| Delete account | Remove a user by ID, with a confirmation step |
| View all users | Lists every registered account and the total count |
| Check a single field | Quick one-off validation without creating an account |

## Field rules

| Field | Rule |
|---|---|
| Name | At least 2 characters, letters and spaces only |
| Username | 4-20 characters, starts with a letter, only letters/digits/underscore, must be unique |
| Email | Standard `name@domain.com` format, must be unique, verified via OTP before account is created |
| Phone | Exactly 10 digits |
| Age | Number between 1 and 120 |
| Password | Minimum 8 characters, needs an uppercase letter, a digit, and a special character — stored as a SHA-256 hash, never in plain text |

## Usage

```bash
python form_checker.py
```

```
===== Smart Form Input Checker - Mini Registration System =====
1. Sign up (create account)
2. Log in
3. Search user
4. Edit profile
5. Delete account
6. View all registered users
7. Just check a single field (no saving)
0. Exit
```

## Example — signing up

```
Enter username: john
  -> Username must be 4-20 characters, try again
Enter username: john_dev
  -> username looks good

Enter email: john@test.com
(simulated) OTP sent to john@test.com: 483920
Enter the OTP to verify your email: 483920
Email verified!

Account created! Your user ID is U1001
```

## Storage

- All accounts are stored in `users.csv` (created automatically on first signup)
- Passwords are stored as SHA-256 hashes — never in readable form
- Each user gets a unique auto-incrementing ID (`U1001`, `U1002`, ...)

## Notes

The OTP here is simulated (printed to the console instead of actually emailed) since there's no mail server involved — but the verification logic itself works exactly like a real one: generate a code, give limited attempts, only proceed once it matches.