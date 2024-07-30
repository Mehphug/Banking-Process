
def show_balance():
    print(f"You balance is ${balance :.2f}")

def deposit():
    amount=float(input("Enter an amount to be deposit :"))
    
    if amount<0:
        print("That's not a valid amount.")
    
    else:
        return amount


def withdraw():
    amount=float(input("Enter amount to be withdrawn :"))
    
    if amount>balance:
        print("Insufficient Funds")
    elif amount<0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
balance=0
is_running=True


while is_running:
    print("Banking Program")
    print("1.show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    choice=input("Enter your choice (1-4) :")
    if choice =='1':
        show_balance()
    elif choice =='2':
        balance+=deposit()
    elif choice =='3':
         balance-=withdraw()
    elif choice =='4':
        is_running==False
    else:
        Print("That is not a valid choice!")
        
        


Print("Thank You! Have a nice day.")