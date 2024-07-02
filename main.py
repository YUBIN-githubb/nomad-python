#파라미터에 디폴트 값 설정해주기
#파라미터에 = 쓰고 뒤에 값을 쓰면 파라미터 값이 아예안들어오거나 조건에 맞지 않게 들어올 경우 디폴트 값으로 실행됨
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
#f""는 중괄호 안의 값을 다른 값으로 대체해서 쓸 수 있음
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

#조건문
#elif는 조건을 여러개 확인할 때 쓰기
#else는 if의 대안 조건
a = 19
b = "yubin"

if a == 19 and b == "yubinn":
  print("correct")

passoword_correct = False

if passoword_correct:
  print("connect success")
else:
  print("worng password")

number = 11

if number > 15:
  print("number is bigger than 10")
elif number < 10:
  print("number is less than 10")
elif number == 10:
  print("number is 10")
else:
  print(number)

#input 연습하기
#input은 하나의 argument만 받아오고 콘솔에 출력 후 입력 된 값을 리턴값으로 받아옴
age = input("how old are you? ")
print("usre age is", age)

#type 연습하기
#파라미터의 타입을 알려줌
print(type(age))

#int 연습하기
#int형으로 형변환 해줌
num = int(input("put a number "))

if num > 10:
  print("num is", num)

#and or 연습하기
drink_age = int(input("what is your drink age? "))
if drink_age >= 18 and drink_age < 60:
  print("you can drink")
elif drink_age < 18 and drink_age >= 0:
  print("you can not drink")
elif drink_age == 60 or drink_age == 70:
  print("you are in danger")

#파이썬 카지노
#built in function과 python standard library 에서 import 해오기

from random import randint

user_choice = int(input("choose number : "))
pc_choice = randint(1,100)

if user_choice == pc_choice:
  print("you win!")
elif user_choice > pc_choice:
  print("you loose. pc choice is", pc_choice)
elif user_choice < pc_choice:
  print("you loose. pc choice is", pc_choice)

#덩어리 주석을 남기려면 큰따옴표 3게

#while 연습하기
distance = 0

while distance < 20:
  print("i'm running", distance, "km")
  distance = distance + 1

#파이썬 카지노 + while
from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1,100)
playing = True

while playing:
  user_choice = int(input("chooser your number in 0 - 100 :"))
  if pc_choice == user_choice:
    print("you win!")
    playing = False
  elif pc_choice > user_choice:
    print("Higher!")
  elif pc_choice < user_choice:
    print("Lower!")


#function과 method
#function은 그냥 함수 method는 데이터 + 함수
name = "nico"
print(name.upper())
print(name.capitalize())

#list 연습하기
day_of_week = ["Mon","Tue","Wed","Thu","Fri"]
print(day_of_week.count("Wed"))
day_of_week.reverse()
print(day_of_week)
day_of_week.clear()
print(day_of_week)