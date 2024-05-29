from random import randint
import time

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.in_transfer = False

    def withdraw(self, value):
        if self.in_transfer == True:
            print("Account in usage")
            return

        self.in_transfer = True
        
        if self.balance >= value:
            self.balance -= value
            print(f"Withdraw value: {value}\t\tNew balance: {self.balance}")
        else:
            print("No founds")

        #Simula o processamento do banco
        sleep = randint(200, 1000)/1000
        time.sleep(sleep)

        self.in_transfer = False

    def deposit(self, value):
        if self.in_transfer == True:
            print("Account in usage")
            return
        
        self.in_transfer = True
        
        self.balance += value
        print(f"Deposit value: {value}\t\tNew balance: {self.balance}")
        
        #Simula o processamento do banco
        sleep = randint(2000, 5000)/1000
        time.sleep(sleep)
        
        self.in_transfer = False

class Transfer:
    _account = None

    @staticmethod
    def set_account(account:Account):
        Transfer._account = account

    @staticmethod
    def get_account():
        return Transfer._account

    @staticmethod
    def withdraw(value):
        if Transfer._account == None:
            print("No account for transfer")
        else:
            Transfer._account.withdraw(value)

    @staticmethod
    def deposit(value):
        if Transfer._account == None:
            print("No account for transfer")
        else:
            Transfer._account.deposit(value)

class RandomTransaction:
    def __init__(self):
        self.thread = None

    def do_transaction(self):
        while True:
            ch = randint(1,2)

            print(self.thread.name)
            match ch:
                case 1:
                    value = randint(100,1000)
                    Transfer.get_account().deposit(value)
                case 2:
                    value = randint(500,1000)
                    Transfer.get_account().withdraw(value)
                case _:
                    print("Invalid Operation")
        
            sleep = randint(500, 2000) / 1000
            time.sleep(sleep)