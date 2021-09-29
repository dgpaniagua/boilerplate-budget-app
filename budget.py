class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance = balance + item["amount"]
    return balance

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount*(-1), "description": description})
      return True
    else:
      return False

  def transfer(self, amount, dest_cat):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to "+dest_cat.name)
      dest_cat.deposit(amount, "Transfer from "+self.name)
      return True
    else:
      return False

  def __str__(self):
    title = self.name.center(30, "*") + "\n"
    item_list = ""
    for item in self.ledger:
      item_list = item_list + item["description"][:23].ljust(23) + str(round(item["amount"], 2)).rjust(7) + "\n"
    total = "Total: " + str(self.get_balance())

    return title + item_list + total

def create_spend_chart(categories):
  total_spent = []
  for cat in categories:
    total_cat = 0
    for item in cat.ledger:
      if item["amount"] < 0:
        total_cat = total_cat - item["amount"]
    total_spent.append(total_cat)


#pruebas intermedias
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

for item in food.ledger:
  print(item["amount"])
print(food.get_balance())
print(food)