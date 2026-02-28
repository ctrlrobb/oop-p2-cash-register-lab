#!/usr/bin/env python3

class CashRegister:
  pass
def __init__(self, discount=0):
     self.discount = discount
     self.total = 0
     self.items = []
     self.previous_transactions = []
     self.last_transaction_amount = 0

def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    self.last_transaction_amount = price * quantity
    self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})
    for _ in range(quantity):
        self.items.append(item)

def apply_discount(self):
    if self.discount > 0:
        self.total = self.total * (100 - self.discount) / 100
        print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
        print("There is no discount to apply.")

def void_last_transaction(self):
    self.total -= self.last_transaction_amount