"""
Basic Encryption Tool - XOR Cipher
------------------------------------
A mini project built to practice Python's Bitwise Operators (^, bytes handling).

Core idea:
    data ^ key = encrypted
    encrypted ^ key = data (back to original)
Same function does both encryption and decryption - just XOR again with the same key.

Features:
1. Encrypt text with a single-character key
2. Decrypt text back using the same key
3. Multi-character (repeating) key XOR - stronger than single char
4. Encrypt/decrypt a whole file and save it (bytes handling)
5. View encrypted output in hex format
6. Try decrypting with a wrong key (shows why the key matters)
7. Save/Load key from a text file
"""

import os


def xor_single_key(data: bytes, key: int) -> bytes:
    """XOR every byte of data with a single integer key (0-255)."""
    return bytes([b ^ key for b in data])


def xor_repeating_key(data: bytes, key: str) -> bytes:
    """XOR data with a repeating multi-character key (like a simple stream cipher)."""
    key_bytes = key.encode("utf-8")
    result = bytearray()
    for i, b in enumerate(data):
        k = key_bytes[i % len(key_bytes)]   # cycle through key characters
        result.append(b ^ k)
    return bytes(result)


def encrypt_text_single_key():
    text = input("Enter text to encrypt: ")
    key = int(input("Enter key (0-255): "))

    data = text.encode("utf-8")
    encrypted = xor_single_key(data, key)

    print("\nEncrypted (raw bytes):", encrypted)
    print("Encrypted (hex):", encrypted.hex())
    return encrypted, key


def decrypt_text_single_key():
    hex_input = input("Enter encrypted text in hex: ").strip()
    key = int(input("Enter key used for encryption (0-255): "))

    try:
        encrypted = bytes.fromhex(hex_input)
    except ValueError:
        print("Invalid hex string.")
        return

    decrypted = xor_single_key(encrypted, key)
    try:
        print("Decrypted text:", decrypted.decode("utf-8"))
    except UnicodeDecodeError:
        print("Wrong key - couldn't decode to readable text. Raw bytes:", decrypted)


def encrypt_text_repeating_key():
    text = input("Enter text to encrypt: ")
    key = input("Enter a key (word/phrase): ")

    data = text.encode("utf-8")
    encrypted = xor_repeating_key(data, key)

    print("\nEncrypted (hex):", encrypted.hex())
    return encrypted, key


def decrypt_text_repeating_key():
    hex_input = input("Enter encrypted text in hex: ").strip()
    key = input("Enter the key used for encryption: ")

    try:
        encrypted = bytes.fromhex(hex_input)
    except ValueError:
        print("Invalid hex string.")
        return

    decrypted = xor_repeating_key(encrypted, key)
    try:
        print("Decrypted text:", decrypted.decode("utf-8"))
    except UnicodeDecodeError:
        print("Wrong key - couldn't decode to readable text. Raw bytes:", decrypted)


def encrypt_file():
    filename = input("Enter filename to encrypt (must exist): ").strip()
    if not os.path.exists(filename):
        print("File not found.")
        return

    key = input("Enter a key (word/phrase): ")

    with open(filename, "rb") as f:
        data = f.read()

    encrypted = xor_repeating_key(data, key)

    out_name = filename + ".enc"
    with open(out_name, "wb") as f:
        f.write(encrypted)

    print(f"File encrypted and saved as {out_name} ({len(encrypted)} bytes)")


def decrypt_file():
    filename = input("Enter encrypted filename (.enc): ").strip()
    if not os.path.exists(filename):
        print("File not found.")
        return

    key = input("Enter the key used for encryption: ")

    with open(filename, "rb") as f:
        data = f.read()

    decrypted = xor_repeating_key(data, key)

    out_name = filename.replace(".enc", ".dec")
    with open(out_name, "wb") as f:
        f.write(decrypted)

    print(f"File decrypted and saved as {out_name} ({len(decrypted)} bytes)")


def demo_wrong_key():
    """Shows what happens when you decrypt with the wrong key."""
    text = "Secret Message"
    right_key = 42

    data = text.encode("utf-8")
    encrypted = xor_single_key(data, right_key)

    wrong_key = 7
    wrong_decrypt = xor_single_key(encrypted, wrong_key)

    print(f"\nOriginal text     : {text}")
    print(f"Encrypted (hex)   : {encrypted.hex()}")
    print(f"Decrypted (correct key {right_key}) : {xor_single_key(encrypted, right_key).decode('utf-8')}")
    try:
        print(f"Decrypted (wrong key {wrong_key})    : {wrong_decrypt.decode('utf-8')}")
    except UnicodeDecodeError:
        print(f"Decrypted (wrong key {wrong_key})    : garbage bytes -> {wrong_decrypt}")


def save_key(key):
    with open("key.txt", "w") as f:
        f.write(str(key))
    print("Key saved to key.txt")


def load_key():
    if not os.path.exists("key.txt"):
        print("No saved key found.")
        return None
    with open("key.txt", "r") as f:
        key = f.read().strip()
    print(f"Loaded key: {key}")
    return key


def show_menu():
    print("\n===== XOR Cipher - Basic Encryption Tool =====")
    print("1. Encrypt text (single-character key)")
    print("2. Decrypt text (single-character key)")
    print("3. Encrypt text (repeating multi-character key)")
    print("4. Decrypt text (repeating multi-character key)")
    print("5. Encrypt a file")
    print("6. Decrypt a file")
    print("7. Demo: Decrypt with wrong key")
    print("8. Save last used key to file")
    print("9. Load key from file")
    print("0. Exit")


def main():
    last_key = None

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            result = encrypt_text_single_key()
            if result:
                last_key = result[1]
        elif choice == "2":
            decrypt_text_single_key()
        elif choice == "3":
            result = encrypt_text_repeating_key()
            if result:
                last_key = result[1]
        elif choice == "4":
            decrypt_text_repeating_key()
        elif choice == "5":
            encrypt_file()
        elif choice == "6":
            decrypt_file()
        elif choice == "7":
            demo_wrong_key()
        elif choice == "8":
            if last_key is not None:
                save_key(last_key)
            else:
                print("No key used yet in this session.")
        elif choice == "9":
            last_key = load_key()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()