#Калькулятор на Python, версия 2.4
print("Привет! Это калькулятор! ")

def again():
  number1 = (input("Введи левый операнд "))
  try: float(number1)
  except: print("Ошибка! Это не число!!!"), exit(0)
  number2 = (input("Введи правый операнд "))
  try: float(number2)
  except: print("Ошибка! Это не число!!!"), exit(0)
  operator = input("Ведите операцию (+, -, *, /, //, %, **, &, |, ^, <<, >>): ") 
  if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**" or operator == "//" or operator == "%" or operator == "&" or operator == "|" or operator == "^" or operator == "<<" or operator == ">>":
    if (operator == "+"): result = number1 + number2
    elif (operator == "-"): result = number1 - number2
    elif (operator == "*"): result = number1 * number2
    elif (operator == "**"): result = number1 ** number2
    elif (operator == "%"): result = number1 % number2
    elif (operator == "&"): result = number1 & number2
    elif (operator == "|"): result = number1 | number2
    elif (operator == "^"): result = number1 ^ number2
    elif (operator == "<<"): result = number1 << number2
    elif (operator == ">>"): result = number1 >> number2
    elif (operator == "/"):
      if (number2 == 0): print("На ноль делить нельзя!"), exit(0)
      else: result = number1 / number2
    elif (operator == "//"):
      if (number2 == 0): print("На ноль делить нельзя!"), exit(0)
      else: result = number1 // number2 , exit(0)
  else: print("Вы неправильно ввели операцию или не ввели её!"), exit(0)
  print("Итог: ", result)
    
Again = "да"
while Again == "да" or Again == "д" or Again == "lf" or Again == "l" or Again == "Да" or Again == "Lf" or Again == "L" or Again == "Д":
  again()
  print("Посчитать ещё раз? (да или нет)")
  Again = input()
