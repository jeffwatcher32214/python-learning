# Build a CLI-based ATM simulation:
# Login with a 4-digit PIN (use a static value like 1234)
# Options after login:
#       Check Balance
#       Deposit
#       Withdraw
#       Exit

PIN_CODE = "1234"
balance = 1000.0

while True:
    for attempt in range(3):
        entered_pin = str(input("Enter your 4-Digit PIN: "))
        if entered_pin == PIN_CODE:
            print("Login Successfull!")
            break
        else:
            print("Incorrect PIN!")
    else:
        print("Too many failed attempts. Exiting...")
        exit()
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Select your option (1-4): "))
    match choice:
        case 1:
            print(f"Your Current Balance: ${balance}")
        case 2:
            deposit_amount = float(input("Enter amount to deposit: "))
            balance += deposit_amount
            print(f"${deposit_amount} deposited successfully!")
        case 3:
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if balance > withdraw_amount and withdraw_amount > 0:
                balance -= deposit_amount
                print(f"${withdraw_amount} withdrawn successfully!")
            elif withdraw_amount < 0:
                print("Invalid amount entered!")
            else:
                print("Aplogies! Insufficient Balance!")
        case 4:
            print("Thank you for using ATM! Good bye!")
            exit()
        case _:
            print("Invalid Input!")