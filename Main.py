import os,time
from accounts import *
from Transaction import *

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def main_loop():
    while True:
        clear()
        print("""
        *********************************
        Welcome To Bank System Management
        *********************************
        Choose an option..
        1. Add account
        2. Delete account
        3. Open account
        4. Exit
        """)
        choice = int(input("Please enter your choice: "))

        if choice==1:
            user = accounts()
            print("Added successfully ✅")

        elif choice==2:
            if len(accounts.users) == 0:
                print("No users added yet 🙂")
            else:
                user_information = input("Please enter wither the ID or the full name of the user which you want to delete it: ")                
                while not accounts.delete_account(user_information):
                    ask = input("Do you want to put another user information (yes or no): ").lower()
                    if ask=="yes":
                        user_information = input("Please enter wither the ID or the full name of the user which you want to delete it: ")
                    elif ask=="no":
                        break
                    else:
                        print("Invalid choice")

        elif choice==3:
            if len(accounts.users) == 0:
                print("No users added yet 🙂")

            else:
                user_information = input("Please enter your ID or your full name: ")
                user = accounts.check_availabe_user(user_information)
                while not user:
                    print("This user is not in our system.. ")
                    ask = input("Do you want to put another user information (yes or no): ").lower()

                    if ask=="yes":
                        user_information = input("Please enter your ID or your full name: ")
                        user = accounts.check_availabe_user(user_information)
                    elif ask=="no":
                        break
                    else:
                        print("Invalid choice")
                true_pass = False
                while user:
                    true_pass = accounts.check_password(user)
                    break


                while user and true_pass:
                    clear()
                    chooce_action = int(input(f"""Welcome to {user.full_name} account's

        1. See account information
        2. Deposit
        3. Withdraw
        4. Transfer Mony (A-->A)
        5. Change the acount name
        6. Change the Password
        7. Exite
        Enter your choice: """))
                    if chooce_action == 1:
                        accounts.display_information(user)
                        time.sleep(2)

                    elif chooce_action == 2:
                        Transaction.depsit(user)

                    elif chooce_action == 3:
                        Transaction.withdraw(user)

                    elif chooce_action == 4:
                        user2 = input("Please enter wither the ID or the full name of the user which you want to transfer the mony to them: ")
                        while not accounts.check_availabe_user(user2):
                            print("Invalid user information")
                            ask = input("Do you want to put another user information (yes or no): ").lower()
                            if ask=="yes":
                                user2 = input("Please enter wither the ID or the full name of the user which you want to transfer the mony to them: ")
                            elif ask=="no":
                                return False
                            else:
                                print("Invalid choice")
                        user2 = accounts.check_availabe_user(user2)
                        if user2:
                            Transaction.transMony(user,user2)


                    elif chooce_action == 5:
                        accounts.change_account_name(user)

                    elif chooce_action == 6:
                        accounts.change_account_password(user)

                    elif chooce_action == 7:
                        print("Why your account look like very poor 😭😭")
                        break

                    else:
                        print("Invalid choice")

                    time.sleep(2)
                


        elif choice==4:
            print("See yoe in next project 👽")
            exit()

        else:
            print("This is not an option 😑")

        print("...")
        time.sleep(3) 
    
main_loop()