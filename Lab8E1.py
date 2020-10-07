# %%

import random

# %%
"""
Q1. Write a TicketMachine class, which models a ticket machine that 
    issues flatfare tickets. The price of a ticket is specified via 
    the constructor (you can use price variable).

    Your TicketMachine class will have the following methods:
        (a) insertMoney, which receives an amount of money from a 
            customer and updates customer’s balance (you can use 
            balance variable).
        (b) getPrice, which return and prints the price of a ticket.
        (c) getBalance, which returns and prints the amount of money 
            already inserted for the ticket
        (d) printTicket, which prints a ticket, update the total 
            collected by the machine and reduce the balance to zero.

The ticket will be printed if the customer’s balance is greater than 
or equal to ticket price. You also need to define a variable 
e.g., total, which keeps track of the total amount of money collected 
by the machine.

Your program should be able to check if the ticket price and the amount 
entered by the customer is valid. For example, ticket price and 
the amount entered by the user cannot be negative.
"""


class TicketMachine:
    def __init__(self):
        self.balance = 0.0
        self.ticket_price = {"SA": 100, "NT": 150,
                             "VIC": 200, "NSW": 300, "QLD": 300}
        answer = 1
        while(answer != 0):
            try:
                print(
                    "Type: \n 1 - Credit money\n 2 - Consult ticket prices\n 3 - Buy ticket\n 4 - Consult balance account")
                answer = int(input("Choose in the menu what you wish:"))
                if answer == 0:
                    break
                elif answer == 1:
                    self.insertMoney(
                        float(input("Type the amount of money you wish to credit in your account:")))
                    print("Account balance: ", self.balance)
                elif(answer == 2):
                    print(self.getprice())
                elif(answer == 3):
                    self.printTicket(
                        input("Choose a destination to buy your:").upper())
                elif(answer == 4):
                    print("Account balance: ", self.balance)
            except ValueError as e:
                print("Something you typed was invalid! try again!")

    def getprice(self):
        ticket_price = "The ticket prices are: \n"
        for i in self.ticket_price.keys():
            ticket_price = ticket_price + "     " + i + ": " + \
                str(self.ticket_price[i]) + " \n"

        return ticket_price

    def insertMoney(self, v):
        if v > 0:
            self.balance = self.balance + v
            return True
        else:
            print("Credit '" + str(v) + "' typed is not valid. Enter again")
            return False

    def printTicket(self, t):
        if t in self.ticket_price.keys():
            if self.balance >= self.ticket_price[t]:
                self.balance = self.balance - self.ticket_price[t]
                print("Ticket", random.randint(1000, 9000),
                      " generated successfully. Your balance is : ", self.balance)
            else:
                print(
                    "You don't have enought balance in your account to buy ticket: '" + t + "'")
        else:
            print("You typed an invalid Ticket: '" + t + "'")


TicketMachine()
