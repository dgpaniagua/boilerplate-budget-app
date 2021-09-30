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
      item_list = item_list + item["description"][:23].ljust(23) + str("{:.2f}".format(item["amount"])).rjust(7) + "\n"
    total = "Total: " + str(self.get_balance())

    return title + item_list + total

def create_spend_chart(categories):
  total_spent = [] #list to store the total spent in each category
  cat_names_rows = 0 #for vertical text
  for cat in categories:
    cat_names_rows = max(cat_names_rows, len(cat.name))
    total_cat = 0
    for item in cat.ledger:
      if item["amount"] < 0: #negative amounts are withdraws
        total_cat -= item["amount"] #it's a rest because they are negatives
    total_spent.append(total_cat)
  for i in range(len(total_spent)): #totals to percetages
    total_spent[i] = (total_spent[i]/sum(total_spent)) * 100
  
  title = "Percentage spent by category"
  lines = [] #list to store each line of the chart body
  base_line = "    "
  j = 0
  for i in reversed(range(0, 101, 10)): #build the body chart
    lines.append(str(i).rjust(3) + "|")
    for tot in total_spent:
      if tot >= i:
        lines[j] = lines[j] + " o "
      else:
        lines[j] = lines[j] + "   "
      if total_spent.index(tot) == len(total_spent) - 1:
        lines[j] = lines[j] + " \n"
    j = j+1
  
  #base line (x-axis)
  for tot in total_spent: 
    if total_spent.index(tot) == len(total_spent) - 1:
      base_line = base_line + "----"
    else:
     base_line = base_line + "---"
  
  #vertical text
  cat_names = "" 
  for i in range(cat_names_rows):
    cat_names += "     "
    for cat in categories:
      if i < len(cat.name):
        cat_names += cat.name[i] + "  "
      else:
        cat_names += "   "
    if i != cat_names_rows - 1:
      cat_names += "\n"
  
  #final string
  spend_car = title + "\n"
  for line in lines:
    spend_car += line
  spend_car += base_line + "\n" + cat_names

  return spend_car