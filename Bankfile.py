#Sai
import random
from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, owner_name, account_no, balance):
        self.__securite_key = 1491485235
        self.customer = owner_name
        self.acc_no = account_no
        self.__balance = balance

    def takemoney(self, amount):
        if self.__securite_key == 1491485235:
            if self.__balance > amount:
                self.__balance -= amount
                print(f"{self.customer} with account number: {self.acc_no} withdraw ${amount}")
            else:
                print("Insufficient Balance")
        else:
            print("INTRUDER!")

    def addmoney(self, amount):
        if self.__securite_key == 1491485235:
            self.__balance += amount
            print(f"{self.customer} with account number: {self.acc_no} deposited ${amount}")
        else:
            print("Thanks for the money man!")

    def balance(self):
        if self.__securite_key == 1491485235:
            print(f"{self.customer} with account number: {self.acc_no} has a balance of ${self.__balance}")
class ATMBase(ABC):
    def __init__(self, account_number, pin, balance):
        self._securitykey = 12498573
        self._account_number = account_number
        self._pin = pin
        self._balance = balance

    @abstractmethod
    def check_balance(self,pin):
        pass
    @abstractmethod
    def deposit(self, pin, amount):
        pass

    @abstractmethod
    def withdraw(self, pin, amount):
        pass
class UserAccount(ATMBase):

    def login(self):
        roasts = ["Wrong again. Your brain is on airplane mode.",
                  "Still wrong. Even ChatGPT can't help you now.",
                  "Are you okay? Blink twice if you forgot your own pin.",
                  "This is a bank, not a guessing game show.",
                  "Bro… go touch grass and try again later.",
                  "You vs correct pin = 0-3. Sit down.",
                  "Even your imaginary friend knows it’s wrong.",
                  "Bet your password is 'password' too."
                  ]

        final_roasts = [ "Wow. 1 fail? You almost had it. Almost.",
                         "2 failed attempts. That’s rookie level disappointment.",
                         "3 times wrong. You’re either bold or just… you.",
                         "4 fails. At this point, I’m rooting *against* you.",
                         "5 misses. GenZBank recommends life decisions review.",
                         "More than 5? You’ve officially been banned from reality."
                         ]

        therapy_links = ["https://genzbank.org/breathe-bro",
                         "https://youdeservetherapy.fakehelp",
                         "https://404.mentalreset.notreal"
                         ]

        attempts = 0
        max_attempts = 5

        while attempts < max_attempts:
            user_pin = int(input("Lets see if you remember your PIN: "))
            if user_pin == self._pin:
                print("Access Granted, Barely")
                return True
            else:
                print(random.choice(roasts))
                attempts += 1

        print("Too many attempts")
        if attempts < len(final_roasts):
            print(final_roasts[attempts])
        else:
            print(final_roasts[-1])

        print("💌 Here is a free therapy sponsored by GenZbank ")
        print(f"{random.choice(therapy_links)}")
        print("Account locked. You dont deserve that money")
        return False

    def check_balance(self, pin):
        if self._securitykey == 12498573 and pin == self._pin:
            print(f"balance in account number: {self._account_number} is ${self._balance}")
        else:
            print("Intruder Alert!")

    def deposit(self, pin, amount):
        if self._securitykey == 12498573 and pin == self._pin:
            self._balance += amount
            print(
                f"Amount of ${amount} has been deposited to account number: {self._account_number} \n Your new balance is now {self._balance:.2f}")
        else:
            print("Thanks for your will to donate man")

    def withdraw(self, pin, amount):
        if self._securitykey == 12498573 and pin == self._pin:
            if amount <= self._balance:
                self._balance -= amount
                print(
                    f"account number: {self._account_number} withdraw amount of ${amount} \n your new balance is now {self._balance:.2f}")
            else:
                print(
                    f"Naa man you're too broke to withdraw that much \n all you have is {self._balance} not a penny more")
        else:
            print(f"Hey dont wish for my money! work for it")
class SavingsAccount(BankAccount):
    def save(self):
        pass