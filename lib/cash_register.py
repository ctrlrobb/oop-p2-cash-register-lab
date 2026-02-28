#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Using the property setter logic for initial validation
        self.discount = discount 
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0  # Defaulting to 0 if invalid

    def add_item(self, item, price, quantity):
        line_total = price * quantity
        self.total += line_total
        self.items.append(item)
        
        # Store as a dictionary for easy access during void/discount
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
            "line_total": line_total
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Calculate discount amount (e.g., 20% of the total)
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        
        # Per requirements: remove the last item from tracking arrays
        last_tx = self.previous_transactions.pop()
        if last_tx['item'] in self.items:
            self.items.remove(last_tx['item'])

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove last transaction and subtract its specific total from the register
        last_tx = self.previous_transactions.pop()
        self.total -= last_tx['line_total']
        
        if last_tx['item'] in self.items:
            self.items.remove(last_tx['item'])