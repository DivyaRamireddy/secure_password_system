# secure_password_system.py
# Password Hashing & Verification using SHA-256 + Salt

import hashlib
import os

user_db = {}

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  # generate random salt
    pwd_hash = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt, pwd_hash

def register_user(username, password):
    if username in user_db:
        return False
    salt, pwd_hash = hash_password(password)
    user_db[username] = (salt, pwd_hash)
    return True

def login_user(username, password):
    if username not in user_db:
        return False
    salt, stored_hash = user_db[username]
    _, pwd_hash = hash_password(password, salt)
    return pwd_hash == stored_hash


def menu():
    print("""
Secure Login System
-------------------
1. Register
2. Login
3. Exit
""")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            if register_user(u, p):
                print("User registered successfully\n")
            else:
                print("User already exists\n")

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            if login_user(u, p):
                print("Login successful ✅\n")
            else:
                print("Invalid credentials ❌\n")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice\n")
