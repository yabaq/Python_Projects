class Bank:
    def __init__(self):
        # Initialize the attributes of the Bank object
        self.client_details_list = []  # List to store client details
        self.loggedin = False  # Flag to track login status
        self.cash = 100  # Initial cash balance
        self.TranferCash = False  # Flag to track transfer cash operation

    def register(self, name, ph, password):
        cash = self.cash
        contitions = True

        # Validate phone number length
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number! Please enter a 10-digit number")
            contitions = True

        # Validate password length
        if len(password) < 5 or len(password) > 18:
            print("Enter a password greater than 5 and less than 18 characters")
            contitions = False

        if contitions == True:
            # Account created successfully
            print("Account created successfully")
            self.client_details_list = [name, ph, password, cash]

            # Store client details in a file
            with open(f"{name}.txt", "w") as f:
                for details in self.client_details_list:
                    f.write(str(details) + "\n")

    def login(self, name, ph, password):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")

            # Verify provided name, phone number, and password against stored client details
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name
            else:
                print("Wrong details")

    def add_cash(self, amount):
        if amount > 0:
            # Add amount to the cash balance
            self.cash += amount

            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            # Update the cash balance in the client details file
            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(
                    str(self.client_details_list[3]), str(self.cash)))

            print("Amount added successfully")
        else:
            print("Enter the correct value of the amount")

    def Tranfer_cash(self, amount, name, ph):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")

            if str(ph) in self.client_details_list:
                self.TranferCash = True

        if self.TranferCash == True:
            # Update balances in both client details files
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount

            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(
                    str(self.client_details_list[3]), str(total_cash)))

            with open(f"{self.name}.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details_2.replace(
                    str(self.client_details_list[3]), str(left_cash)))

            print("Amount Transferred Successfully to", name, "-", ph)
            print("Balance left =", left_cash)
            self.cash = left_cash

    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter a password greater than 5 and less than 18 characters")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            # Update the password in the client details file
            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(
                    str(self.client_details_list[2]), str(password)))
            print("New password set up successfully")

    def ph_change(self, ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number! Please enter a 10-digit number")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            # Update the phone number in the client details file
            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(
                    str(self.client_details_list[1]), str(ph)))
            print("New Phone number set up successfully")


if __name__ == "__main__":
    Bank_object = Bank()

    print("Welcome to my Bank")
    print("1. Login")
    print("2. Create a new Account")
    user = int(input("Make a decision: "))

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")

        # Attempt to login with provided details
        Bank_object.login(name, ph, password)

        while True:
            if Bank_object.loggedin:
                print("1. Add amount")
                print("2. Check Balance")
                print("3. Transfer amount")
                print("4. Edit profile")
                print("5. Logout")
                login_user = int(input())

                if login_user == 1:
                    print("Balance =", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)

                    print("\n1. Back to menu")
                    print("2. Logout")
                    choose = int(input())

                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 2:
                    print("Balance =", Bank_object.cash)
                    print("\n1. Back to menu")
                    print("2. Logout")
                    choose = int(input())

                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print("Balance =", Bank_object.cash)
                    amount = int(input("Enter amount: "))

                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Tranfer_cash(amount, name, ph)

                        print("\n1. Back to menu")
                        print("2. Logout")
                        choose = int(input())

                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0:
                        print("Enter the correct value of the amount")
                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif login_user == 4:
                    print("1. Password change")
                    print("2. Phone Number change")
                    edit_profile = int(input())

                    if edit_profile == 1:
                        new_password = input("Enter new Password: ")
                        Bank_object.password_change(new_password)

                        print("\n1. Back to menu")
                        print("2. Logout")
                        choose = int(input())

                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)

                        print("\n1. Back to menu")
                        print("2. Logout")
                        choose = int(input())

                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 5:
                    break

    if user == 2:
        print("Creating a new Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")

        # Register a new account with provided details
        Bank_object.register(name, ph, password)
