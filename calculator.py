#Калькулятор на Python, версия 2.5
print("Привет! Это калькулятор! ") #Приветствие

def again(): #Повторение
  number1 = (input("Введи левый операнд ")) #Ввод первого числа
  try: float(number1) #Если это число - преобразуем в дробное
  except: print("Ошибка! Это не число!!!"), exit(0) #Иначе - выдаст ошибку. Выход из программы
  number2 = (input("Введи правый операнд ")) #Ввод второго числа
  try: float(number2) #Если это число - преобразуем в дробное
  except: print("Ошибка! Это не число!!!"), exit(0) #Иначе - выдаст ошибку. Выход из программы
  operator = input("Ведите операцию (+, -, *, /, //, %, **, &, |, ^, <<, >>): ") #Ввод операторов из списка предложенных 
  if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**" or operator == "//" or operator == "%" or operator == "&" or operator == "|" or operator == "^" or operator == "<<" or operator == ">>": #Проверяем те ли это операторы. Если те - то
    if (operator == "+"): result = number1 + number2  #Плюс - складываем и записываем в переменную result результат
    elif (operator == "-"): result = number1 - number2 #Минус - вычитаем и записываем в переменную result результат
    elif (operator == "*"): result = number1 * number2 #И т.д.
    elif (operator == "**"): result = number1 ** number2
    elif (operator == "%"): result = number1 % number2
    elif (operator == "&"): result = number1 & number2
    elif (operator == "|"): result = number1 | number2
    elif (operator == "^"): result = number1 ^ number2
    elif (operator == "<<"): result = number1 << number2
    elif (operator == ">>"): result = number1 >> number2
    elif (operator == "/"):
      if (number2 == 0): print("На ноль делить нельзя!"), exit(0) #Проверка на ноль. Есть - ошибка. Выход из программы
      else: result = number1 / number2 #Иначе делим и записываем результат
    elif (operator == "//"): 
      if (number2 == 0): print("На ноль делить нельзя!"), exit(0) #Проверка на ноль.
      else: result = number1 // number2 #Записываем.
  else: print("Вы неправильно ввели операцию или не ввели её!"), exit(0) #Иначе - ошибка. Выход
  print("Итог: ", result) #Выводим результат
    
again2 = "да" #Переменная. Хочет ли пользователь продолжать дальше подсчёт
while again2 == "да" or again2 == "д" or again2 == "lf" or again2 == "l" or again2 == "Да" or again2 == "Lf" or again2 == "L" or again2 == "Д": #Проверка
  again() #Вызываем функцию, если пользователь согласен
  again2 = input(("Посчитать ещё раз? (да или нет)")) #Задаём вопрос
  #Иначе завершение программы
