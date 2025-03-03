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