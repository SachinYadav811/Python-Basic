import os
import json

ACCOUNTS_FILE = "accounts.txt"

# Load accounts from file
def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)

# Save accounts to file
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# Create a new account
def create_account(accounts):
    acc_number = input("Enter new account number: ")
    if acc_number in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit amount: "))
    accounts[acc_number] = {
        "name": name,
        "balance": balance
    }
    print("Account created successfully!")

# Deposit money
def deposit(accounts):
    acc_number = input("Enter account number: ")
    if acc_number not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter amount to deposit: "))
    accounts[acc_number]["balance"] += amount
    print("Deposit successful!")

# Withdraw money
def withdraw(accounts):
    acc_number = input("Enter account number: ")
    if acc_number not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter amount to withdraw: "))
    if accounts[acc_number]["balance"] < amount:
        print("Insufficient balance!")
        return
    accounts[acc_number]["balance"] -= amount
    print("Withdrawal successful!")

# Check balance
def check_balance(accounts):
    acc_number = input("Enter account number: ")
    if acc_number not in accounts:
        print("Account not found!")
        return
    acc = accounts[acc_number]
    print(f"Account Holder: {acc['name']}")
    print(f"Balance: ${acc['balance']:.2f}")

# Menu
def main():
    accounts = load_accounts()
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            save_accounts(accounts)
            print("Thank you for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
