#Калькулятор на Python, версия 2.1
print("Привет! Это калькулятор! ")
number1 = (input("Введи левый операнд "))
try: float(number1)
except: print("Ошибка! Это не число!!!"), exit(0)
number2 = (input("Введи правый операнд "))
try: float(number2)
except: print("Ошибка! Это не число!!!"), exit(0)
operator = input("Ведите операцию (+, -, *, /, **): ") 
if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**":
    if (operator == "+"): result = number1 + number2
    elif (operator == "-"): result = number1 - number2
    elif (operator == "*"): result = number1 * number2
    elif (operator == "**"): result = number1 ** number2
    elif (operator == "/"):
        if (number2 == 0): print("На ноль делить нельзя!")
        else: result = number1 / number2
else: print("Вы неправильно ввели операцию или не ввели её!"), exit(0)
print("Итог: ", result)

