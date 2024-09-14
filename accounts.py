import time

class accounts():
    users = []

    def __init__(self):
        self.full_name = accounts.checks_and_set(1)
        self.ID = self.set_ID()
        self.password = accounts.checks_and_set(3)
        self.balance = accounts.checks_and_set(2)       
        accounts.users.append(self)

    def show_details(self):
        print(f"Account name: {self.full_name}")
        print(f"Account ID: {self.ID}")
        print(f"Account balance: {self.balance}")

    @staticmethod
    def checks_and_set(mode):
        if mode==1:
            name = input("Please enter your name (without any special character): ")
            while not name.isalpha():
                print("Invalid name 🤔")
                name = input("Please enter your name (without any special character): ")
            return name


        elif mode==2:
            balance = float(input("Please enter your balance (Postive number only): "))
            while balance < 0.0:
                print("Invalid balance 🤔")
                name = float(input("Please enter your balance (Postive number only): "))
            return balance


        else:
            password = input("Please enter your password (Must be more than 6 characters): ")
            while len(password) <= 6:
                print("Invalid length of password 🤔")
                password = input("Please enter your password (Postive number only): ")
            return password

                
    def set_ID(self):
        while True:
            ID = 0
            for user in accounts.users:
                if user.ID == ID:
                    ID+=1
                else:
                    return ID
            return ID


    @staticmethod
    def check_availabe_user(user_information):
        if user_information.isdigit():
            user_information = int(user_information)
            for user in accounts.users:
                if user.ID == user_information:
                    return user


        else:
            for user in accounts.users:
                if user.full_name == user_information:
                    return user

        return False



    @staticmethod
    def check_password(user):
        password = input(f"Please enter the password for this user account name ({user.full_name}): ")
        while password != user.password:
            chance = 3
            for i in range(3):
                print(f"Wrong password you still have {chance} chances")
                password = input(f"Please enter the password for this user account name ({user.full_name}): ")
                chance -= 1
                if password == user.password:
                    return True
            print("Sorry but you try to access for an account wich is not yours 🤬")
            return False
        return True





    @staticmethod
    def delete_account(user_information):
        user = accounts.check_availabe_user(user_information)
        if user:
            if accounts.check_password(user):
                accounts.users.remove(user)
                print(f"Done the delete user with name ({user.full_name}) by his ID {user.ID} ✅")
                return True
        else:
            print("This user is not in our system.. ")

        return False

    @staticmethod
    def change_account_name(user):
        new_name = input("Please enter the new account name (without any special character): ")
        while not new_name.isalpha():
            print("Invalid name 🤔")
            new_name = input("Please enter the new account name (((without any special character)))): ")
        user.full_name = new_name
        print("Done ✅")


    @staticmethod
    def change_account_password(user):
        new_password = input("Please enter your new account password (at leest 7 characters): ")
        while len(new_password) < 7:
            print("Invalid length password ❌")
            new_password = input("Please enter your new account password (((at leest 7 characters))): ")
        user.password = new_password
        print("Done ✅")


    @staticmethod
    def display_information(user):
        print(f"The account name: {user.full_name}")
        print(f"The account ID: {user.ID}")
        print(f"The account passowrd: {user.password}")
        print(f"The account balance: {user.balance}")

            


