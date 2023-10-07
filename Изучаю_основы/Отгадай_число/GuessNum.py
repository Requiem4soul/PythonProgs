import random

b=0
c=0
b = print("Введите левую границу диапозона:")
b = int(input())
c = print("Введите правую границу диапозона:")
c = int(input())
d = 0
a = random.randint(b, c)



e = False

while e != True:
        print("Отгадай моё число\n")
        d = int(input())
        if d == a:
                e==True
                print("Ты угадал, моё число: " + str(a) + "!\n")
                break
        else:
                print("Не угадал, давай ещё\n")
                