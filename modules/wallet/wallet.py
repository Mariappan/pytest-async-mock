#!/usr/bin/env python3

class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount
        self.debugmsg(f"Initial balance is {self.balance}")

    def debugmsg(self, msg):
        print("WALLET: " + msg)

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Insufficient funds: {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
