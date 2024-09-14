class Transaction():
    @staticmethod   
    def depsit(user):
        mony = int(input("How much you want to depsit to your acount (Postive Integer): "))
        while mony<0:
            print("Invalid amount 🤔")
            mony = int(input("How much you want to depsit to your acount (Postive Integer): "))
        user.balance = user.balance + mony
        print("Done ✅")

    @staticmethod
    def withdraw(user):
        mony = int(input("How much you want to withdraw from your acount (Postive Integer and Less than your balance): "))
        while mony<0 or mony>user.balance:
            print("Invalid amount 🤔")
            mony = int(input("How much you want to withdraw from your acount (Postive Integer): "))
        user.balance = user.balance - mony
        print("Done ✅")

    @staticmethod
    def transMony(user1 , user2):
        mony = int(input(f"How much mony you want to give {user2.full_name} from your acount (Postive Integer and Less than your balance): "))
        while mony<0 or mony>user1.balance:
            print("Invalid amount 🤔")
            mony = int(input("How much you want to withdraw from your acount (Postive Integer): "))
        user1.balance = user1.balance - mony
        user2.balance = user2.balance + mony
        print("Done ✅")

