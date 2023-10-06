by = False
while by!= True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Введите операцию из +,-,/,*,**,//,%: ")
    if operation == "+":
        print(a + b)
    if operation == "-":
        print(a - b)
    if operation == "*":
        print(a * b)
    if operation == "/":
        print(a / b)
    if operation == "**":
        print(a ** b)
    if operation == "//":
        print(a // b)
    if operation == "%":
        print(a % b)
    if operation != "+" and operation != "-" and operation!= "*" and operation!= "/" and operation!= "%" and operation!= "//" and operation!= "**":
        print("Неверная операция")
    print("Желаете ещё раз? (Да/Нет)")
    if input() == "Да":
        by = False
    else:
        by = True
        print("Программа завершила свою работу\nУдачи!")


