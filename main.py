def UserSpace(username):
    while True:
        print(f"Welcome {username}. Please select an operation\n")
        print("(1): Send assimilates\n")
        print("(2): Check balance\n")
        print("(3): See Transactions\n")
        print("(4): Logout\n")
        operation = input(">>> ")
        match operation:
            case '1':
                SendCoin()
            case '2':
                CheckBalance()
            case '3':
                SeeAllTransactions()
            case '4':
                UserLogout()

def SendCoin():
    print("Select the recipeint and the amount you wish to send")
    #showAllUsers() - calls a databse search function
    value = input("value: ")
    recipient = input("recipient: ")
    #will add validation checks later to see if user exists/is spelled right, with a validation on our balance.
    CreateTransaction(value, recipient)
return None

    



def UserLogin():
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if (username == 'admin' and password == '123'):
        print("Login successful.")
        UserSpace(username)
    return None

def UserLogout():
    print("Loging out...")
    main()
    return None

def main():
    while True:
        print("Select an option: ")
        print("(1): Login")
        print("(2): Exit")
        option = input(">>> ")
        match option:
            case '1':
                UserLogin()
            case '2':
                exit()



            

