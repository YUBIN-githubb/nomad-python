#파라미터에 디폴트 값 설정해주기
def plus(a = 0, b = 0):
  print(a + b)

def minus(a = 0, b = 0):
  print(a - b)

def multiple(a = 0, b = 0):
  print(a * b)

def divide(a = 1, b = 1):
  print(a / b)

def powerof(a = 0, b = 0):
  print(a ** b)

def tax_calculator(money):
  return money * 0.4

def pay_tax(tax):
  print("thank you for paying", tax)

pay_tax(tax_calculator(150))

#f"" 연습하기
def make_juice(fruit):
  return f"{fruit} + 🥤"

def add_ice(juice):
  return f"{juice} + 🧊"

def add_sugar(iced_juice):
  return f"{iced_juice} + 🍭"

juice = make_juice("🍇")
print(juice)
iced_juice = add_ice(juice)
print(iced_juice)
print(add_sugar(iced_juice))