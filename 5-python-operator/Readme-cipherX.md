# 🔐 CipherX — Basic Encryption Tool (XOR Cipher)

A Python CLI project built to practice **Bitwise Operators** — specifically XOR (`^`) — by building a real, working encryption/decryption tool from scratch.

---

## 📌 Overview

CipherX uses the XOR bitwise operator's unique property to encrypt and decrypt text or files with a key. No external libraries, no black-box magic — pure bitwise logic.

**Core Principle:**
```
data ^ key = encrypted
encrypted ^ key = data (back to original)
```

The **same function** handles both encryption and decryption — just XOR again with the same key.

---

## ✨ Features

| # | Feature | Description |
|---|---|---|
| 1 | Encrypt text (single-char key) | Basic XOR with an integer key (0–255) |
| 2 | Decrypt text (single-char key) | Reverses encryption using the same key |
| 3 | Encrypt text (repeating key) | Multi-character key cycled across data (stream-cipher style) |
| 4 | Decrypt text (repeating key) | Reverses multi-character key encryption |
| 5 | Encrypt a file | Reads any file as bytes, XORs, and saves as `.enc` |
| 6 | Decrypt a file | Reverses file encryption, saves as `.dec` |
| 7 | Wrong-key demo | Shows what garbage output looks like with an incorrect key |
| 8 | Save key to file | Stores last-used key in `key.txt` |
| 9 | Load key from file | Reloads a previously saved key |

---

## 🛠️ How It Works

- Text is converted to **bytes**, then each byte is XORed with the key's byte value.
- **Single-character key** → same integer key applied to every byte.
- **Repeating key** → key characters cycle across the data (`key[i % len(key)]`), similar to a basic stream cipher — stronger than a single-byte key.
- **Files** are read/written in binary mode (`rb`/`wb`) so it works on any file type, not just text.
- Encrypted output can be viewed as a **hex string** for easy copying/sharing.

---

## 🚀 Usage

```bash
python cipherX.py
```

Menu:
```
===== CipherX - Basic Encryption Tool =====
1. Encrypt text (single-character key)
2. Decrypt text (single-character key)
3. Encrypt text (repeating multi-character key)
4. Decrypt text (repeating multi-character key)
5. Encrypt a file
6. Decrypt a file
7. Demo: Decrypt with wrong key
8. Save last used key to file
9. Load key from file
0. Exit
```

---

## 📖 Example

```
Enter text to encrypt: Hello
Enter key (0-255): 42

Encrypted (hex): 62696722

--- later ---

Enter encrypted text in hex: 62696722
Enter key used for encryption (0-255): 42

Decrypted text: Hello
```

Try decrypting with the **wrong key** (option 7) to see why the key matters — you'll get unreadable garbage output instead of the original text.

---

## 📂 Files Generated

| File | Description |
|---|---|
| `<filename>.enc` | Encrypted version of an input file |
| `<filename>.dec` | Decrypted version of an `.enc` file |
| `key.txt` | Saved encryption key |

---

## 🧠 What I Learned

- How **bitwise XOR** works at the byte level and why it's reversible with the same key
- Difference between a **single-byte key** and a **repeating-key stream cipher**
- Handling raw **binary data** (`bytes`/`bytearray`) for text and files alike
- Why encryption without the correct key produces meaningless output — the foundation of basic symmetric ciphers

> ⚠️ Note: This is an educational project to understand bitwise operators, not a production-grade encryption tool. Real-world security uses far stronger algorithms (AES, RSA, etc.).

---

## 🔗 Author

Built as part of my self-paced Python learning journey — notes and projects tracked on GitHub.