class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    balance = 0
    for item in self.ledger:
      balance = balance + item["amount"]
    
    if balance >= amount:
      self.ledger.append({"amount": amount*(-1), "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance = balance + item["amount"]
    return balance


#def create_spend_chart(categories):

#pruebas intermedias
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

for item in food.ledger:
  print(item["amount"])
print(food.get_balance())