fact = 1.0
again = False
while again!= True:
    x = input("Введите число, факториал которого будет вычислено: ")
    while float(x) != 1:
        fact = fact * float(x)
        x = float(x) - 1

    print("Факториал этого числа равен: " + str(fact))
    fact = 1.0
    print("Желаете повторить? (Да/Нет)")
    if input() == "Нет":
        again = True
