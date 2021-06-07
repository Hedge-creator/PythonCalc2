print("Привет! Это калькулятор! ")
number1 = float(input("Введи левый операнд "))
number2 = float(input("Введи правый операнд "))
operator = input("Ведите операцию (+, -, *, /, **): ") 
if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**":
    if (operator == "+"): result = number1 + number2
    elif (operator == "-"): result = number1 - number2
    elif (operator == "*"): result = number1 * number2
    elif (operator == "**"): result = number1 ** number2
    elif (operator == "/"):
        if (number2 == 0): print("На ноль делить нельзя!")
        else: result = number1 / number2
else:
  print("Вы неправильно ввели операцию или ничего не ввели! Попробуйте ещё раз.")
print("Итог: ", result)
