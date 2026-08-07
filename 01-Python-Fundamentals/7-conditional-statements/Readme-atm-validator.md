# ATM Cash Withdrawal Validator

A CLI-based ATM simulator built in Python — checks your PIN, validates withdrawal rules, tracks daily limits, and even breaks your cash into notes like a real ATM would.

## Why this exists

Every ATM runs a bunch of conditions before it hands you cash — is your PIN right, do you have enough balance, are you within your daily limit, can the machine even give you that exact amount in notes? This project recreates that whole decision chain using conditional statements.

## Rules it enforces

| Check | Rule |
|---|---|
| PIN | 4-digit PIN, 3 attempts before the card gets blocked |
| Minimum withdrawal | Rs. 100 |
| Amount format | Must be in multiples of 100 |
| Per-transaction limit | Max Rs. 10,000 in a single withdrawal |
| Balance check | Can't withdraw more than what's available |
| Daily limit | Max Rs. 25,000 total per day (tracked across transactions) |
| Denomination check | Amount must be dispensable using 500/200/100 notes |

## Features

- **Withdraw cash** — runs through every check above, and if it all passes, shows exactly how many 500/200/100 notes you'll get
- **Check balance** — view current account balance
- **Deposit cash** — add money to the account
- **Today's transactions** — see every withdrawal made today and how much of your daily limit is left

## Usage

```bash
python atm_validator.py
```

```
Welcome to Quick ATM
Enter your 4-digit PIN: ****

===== ATM Machine =====
1. Withdraw Cash
2. Check Balance
3. Deposit Cash
4. Today's Transactions
0. Exit
```

## Example

```
Enter amount to withdraw: Rs. 1700

Please collect your cash:
  3 x Rs.500 notes
  1 x Rs.200 note

Withdrawal successful. Remaining balance: Rs. 48300
```

## Files

- `account.txt` — stores the current balance (starts at Rs. 50,000 on first run)
- `transactions.txt` — logs every withdrawal with the date, used to calculate the daily limit

## Notes

The PIN and starting balance are hardcoded for this simulation since there's no real bank backend involved — but the actual validation logic (limits, balance checks, denomination breakdown) works exactly like a real ATM's decision flow.