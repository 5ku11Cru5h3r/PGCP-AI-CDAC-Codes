AUDIT_TRANSACTION_COUNT = 0
def create_bank_account(owner_name, initial_balance)->dict:
    balance=float(initial_balance)
    history=[f"Account created with {balance}"]

    def deposit(amount):
       global AUDIT_TRANSACTION_COUNT
       nonlocal balance,history
       balance+=amount
       history.append(f"Deposited {amount}")
       AUDIT_TRANSACTION_COUNT+=1
    def withdraw(amount):
        global AUDIT_TRANSACTION_COUNT
        nonlocal balance,history
        if balance>=amount:
            balance-=amount
            history.append(f"withdrawn {amount}")
            AUDIT_TRANSACTION_COUNT+=1
        else:
            raise ValueError("Insufficient Balance")
    def get_statement():
        nonlocal history
        return (owner_name,balance,history.copy())
    return {
        "deposit":deposit,
        "withdraw":withdraw,
        "statement": get_statement

    }
owner_name=input("Enter the account holder name: ")
initial_balance=float(input("Enter the initial balance: "))
acc=create_bank_account(owner_name,initial_balance)
print("\Account created Successfully")
deposit_amount=float(input("Enter the deposit amount: "))
acc["deposit"](deposit_amount)
withdraw_amount=float(input("Enter the amount to withdraw: "))
try: 
    acc['withdraw'](withdraw_amount)
except ValueError as e:
    print(e)
owner,balance,history=acc['statement']()
print("-----ACCOUNT DETAILS-----")
print("Owner: ",owner)
print("Balance: ",balance)
print("History: ",history)
print("Number of transactions : ",AUDIT_TRANSACTION_COUNT)