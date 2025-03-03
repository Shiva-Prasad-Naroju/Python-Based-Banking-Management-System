import datetime

class Sbi:
    bank_name = 'SBI'
    ifsc_code = 'SBI1230'
    location = 'dilsuknagar'
    no_of_customers = 0

    customer_data = {}     # key : value
    transaction_data = dict()

    def __init__(self,name,age,phone,aadhar,pin,address,balance):
        self.name = name
        self.age = age
        self.phone = self.validate_phone(phone)
        self.aadhar = self.validate_aadhar(aadhar)
        self.pin = self.validate_pin(pin)
        self.address = address
        self.balance = balance

        self.cust_no_increment()

        self.acc_num = 1001 + self.no_of_customers

        self.storing_data(self.acc_num,self)
    @classmethod
    def cust_no_increment(cls):
        cls.no_of_customers+=1

    @classmethod
    def storing_data(cls,acc_num,object_address):
        cls.customer_data[acc_num] = object_address     # dictionary syntax

    @staticmethod
    def validate_phone(phone_num):
        if len(str(phone_num)) == 10 and str(phone_num).isdigit():
            return phone_num
        else:
            raise Exception('INVALID NUMBER')
        
    @staticmethod
    def validate_aadhar(aadhar_num):
        if len(str(aadhar_num)) == 12 and str(aadhar_num).isdigit():
            return aadhar_num
        else:
            raise Exception('INVALID AADHAR NUMBER')
    @staticmethod
    def validate_pin(pin_num):
        if len(str(pin_num)) == 4 and str(pin_num).isdigit():
            return pin_num
        else:
            raise Exception('INVALID PIN')
        
    @classmethod
    def create_account(cls):
        aadhar_number = int(input('ENTER 12-DIGIT AADHAR NUMBER : '))

        for acc_num in cls.customer_data:
            if aadhar_number == cls.customer_data[acc_num].aadhar:
                print('Aadhar number already exists')
                break
        else:
            name = input('Enter your name : ')
            age = int(input('Enter your age : '))
            phone = int(input('Enter your 10-digit phone number : '))
            pin = int(input('Enter 4-digit pin number : '))
            address = input('Enter your address  : ')
            minimum_bal = int(input('Enter the amount : '))

            var = cls(name,age,phone,pin,address,minimum_bal)

    @classmethod
    def user_balance(cls):
        print('--------------------------  BALANCE PAGE  --------------------------')
        user_acc_num = int(input('Enter your account_num : '))
        user_pin = int(input('Enter your 4-digit pin  : '))

        if user_acc_num in cls.customer_data and cls.customer_data[user_acc_num].pin == user_pin:
            print(f'Your current balance is {cls.customer_data[user_acc_num].balance}')
        else:
            raise Exception('INVALID USER')
    
    @classmethod
    def deposit(cls,chance=1):
        print('-------------------------DEPOSIT PAGE-------------------------')
        if chance == 4:
            print('Attempts over')
            return

        user_acc_num = int(input('Enter user account number :'))
        user_pin = int(input('Enter user pin :  '))

        if user_acc_num in cls.customer_data and cls.customer_data[user_acc_num].pin == user_pin:
            amount = int(input('Enter amount to deposit  :'))

            if amount > 0:
                cls.customer_data[user_acc_num].balance += amount
                print(f'Rs.{amount} have been credited,'
                      f'Your current balance is {cls.customer_data[user_acc_num].balance} ')

                if user_acc_num not in cls.transaction_data:
                    cls.transaction_data[user_acc_num] = [{'DATE_TIME' : datetime.datetime.now(),
                                                           'TYPE' : 'CREDIT',
                                                           'AMOUNT' : amount,
                                                           'BALANCE' : cls.customer_data[user_acc_num].balance}]
                else:
                    cls.transaction_data[user_acc_num] += [{'DATE_TIME' : datetime.datetime.now(),
                                                           'TYPE' : 'CREDIT',
                                                           'AMOUNT' : amount,
                                                           'BALANCE' : cls.customer_data[user_acc_num].balance}]
            else:
                print('INVALID AMOUNT')

        else:
            print('INVALID USER')
            cls.deposit(chance + 1)

    @classmethod
    def withdraw(cls, chance = 1):
        print('-------------------------WITHDRAW PAGE-------------------------')
        if chance == 4:
            print('Attempts over')
            return
        user_acc_num = int(input('Enter user account number : '))
        user_pin = int(input('Enter user pin : '))

        if user_acc_num in cls.customer_data and cls.customer_data[user_acc_num].pin == user_pin:
            amount = int(input('Enter amount to withdraw : '))

            if amount <= cls.customer_data[user_acc_num].balance:
                cls.customer_data[user_acc_num].balance -= amount
                print(f'Rs.{amount} have been debited from your account, '
                      f'Your current balance is : {cls.customer_data[user_acc_num].balance}')

                if user_acc_num not in cls.transaction_data:
                    cls.transaction_data[user_acc_num] = [{'DATE_TIME' : datetime.datetime.now(),
                                                           'TYPE' : 'CREDIT',
                                                           'AMOUNT' : amount,
                                                           'BALANCE' : cls.customer_data[user_acc_num].balance}]

                else:
                    cls.transaction_data[user_acc_num]  += [{'DATE_TIME' : datetime.datetime.now(),
                                                           'TYPE' : 'CREDIT',
                                                           'AMOUNT' : amount,
                                                           'BALANCE' : cls.customer_data[user_acc_num].balance}]

            else:
                print('Insufficient balance')
        else:
            print('Invalid user')
            cls.withdraw(chance + 1)

    @classmethod
    def change_pin(cls):
        print('-------------------------CHANGE PIN--------------------------------')

        user_acc_num = int(input('Enter user account number : '))
        user_pin = int(input('Enter user pin number : '))

        if user_acc_num in cls.customer_data and cls.customer_data[user_acc_num].pin == user_pin:
            new_pin = int(input('Enter your new pin : '))
            confirm_pin = int(input('Confirm your new pin : '))

            if new_pin == confirm_pin:
                cls.customer_data[user_acc_num].pin = new_pin
                print('PIN CHANGED SUCCESSFULLY')

            else:
                print('New pin and Confirm pin are not matching')
        else:
            print('INVALID USER')

    @classmethod
    def user_details_modification(cls):
        print('--------------------MODIFICATION PAGE--------------------')

        user_acc_num = int(input('Enter user account number : '))
        user_pin = int(input('Enter user pin number  :'))
        if user_acc_num in cls.customer_data and cls.customer_data[user_acc_num].pin == user_pin:
            print('/n SELECT 1 : TO CHANGE THE NAME', 'SELECT 2 : TO CHANGE THE ADDRESS','SELECT 2 : TO CHANGE THE PHONE\n',sep = '\n')

            select_option = int(input('Enter a number : '))
            match select_option:
                case 1:
                    print('------------------CHANGE THE NAME-------------------')

                    new_name = input('ENTER YOUR NEW NAME : ')
                    confirm_name = input('RE-ENTER YOUR NEW NAME : ')

                    if new_name == confirm_name:
                        cls.customer_data[user_acc_num].name = new_name
                        print(f'Your name has changed successfully to {cls.customer_data[user_acc_num].name}')
                    else:
                        print('New name and confirm name are not matching')

                case 2:
                    print('------------------CHANGE THE ADDRESS-------------------')

                    new_address = input('ENTER YOUR NEW ADDRESS')
                    confirm_address = input('RE-ENTER YOUR NEW ADDRESS ')

                    if new_address == confirm_address:
                        cls.customer_data[user_acc_num].address = new_address
                        print('Your address has changed successfully')
                    else:
                        print('new address and confirm address are not matching')
                case 3:
                    print('------------------CHANGE THE PHONE------------------------')

                    new_phone = int(input('ENTER YOUR NEW PHONE NUMBER'))
                    confirm_new_phone = int(input('CONFIRM YOUR NEW PHONE NUMBER'))

                    if new_phone == confirm_new_phone:
                        cls.customer_data[user_acc_num].phone = new_phone
                        print('Your phone number has changed successfully')
                    else:
                        print('New phone number and confirm phone number are not matching')

                case _:
                    print('SELECT THE OPTION FROM (1,2,3)')
        else:
            print('INVALID USER')

    @classmethod
    def transfer_money(cls):
        print('----------------------TRANSFER MONEY PAGE -------------------------')
        sender_acc_num = int(input('Enter user account number :'))
        sender_pin = int(input('Enter user pin number  :'))

        if sender_acc_num in cls.customer_data and cls.customer_data[sender_acc_num].pin == sender_pin:
            receiver_acc_num = int(input('Enter receiver account number : '))
            receiver_ifsc_num = input('Enter ifsc code : ')

            if receiver_acc_num in cls.customer_data and receiver_ifsc_num == cls.customer_data[receiver_acc_num].ifsc_code:
                amount = int(input('Enter amount to transfer  :'))

                if amount <= cls.customer_data[sender_acc_num].balance:
                    cls.customer_data[sender_acc_num].balance -= amount
                    cls.customer_data[receiver_acc_num].balance += amount
                    print(f'Rs.{amount} transferred successfully to {cls.customer_data[receiver_acc_num].name}')

                    print()
                    print(cls.customer_data[sender_acc_num].balance, 'shiva')
                    print(cls.customer_data[receiver_acc_num].balance, 'hahaha')

                else:
                    print('Insufficient balance')
            else:
                print('Receiver account not found')
        else:
            print('INVALID USER')
    @classmethod
    def mini_statement(cls):
        print('-----------------------MINI STATEMENT PAGE-----------------------')

        user_acc_num = int(input('Enter user account number  : '))
        user_pin = int(input('Enter user pin  : '))

        if user_acc_num in cls.customer_data and cls.customer_data[user_acc_num].pin == user_pin:
            print('DATE_TIME'.ljust(20),'TYPE'.center(16), 'AMOUNT'.center(20),'BALANCE'.center(10), sep =" | ")

            transaction_history = cls.transaction_data[user_acc_num]

            for d in transaction_history:
                print(d['DATE_TIME'],d['TYPE'].center(16),str(d['AMOUNT'].center(20),str(d['BALANCE'].center(10))))
        else:
            print('INVALID ACCOUNT')


c1 = Sbi('Shiva',22,9603253185,819960899888,9009,'Hyderabad',90000)
c2 = Sbi('Elon',30,1111111111,121212121212,9000,'Mars',9090)
c3 = Sbi('Mark',29,1212121212,121212121212,8787,'Earth',8787)

c1.mini_statement()

c2.create_account()


c1.deposit()
print(c1.transaction_data)

c1.deposit()
print(c1.transaction_data)

c1.withdraw()
print(c1.transaction_data)
