import math

a=False
numbers = []


left = 0
right =  100
print("Задайте самое малое число из угадаевымых, но больше 0")
left = int(input())
print("Задайте самое большое число из угадаевымых, но больше 0")
right = int(input())
leftn=left
rightn=right
midle=(right-left+1)/2


for leftn in range(leftn,rightn+1):
    numbers.append(leftn)
print(numbers)
leftn=left
rightn=right
midle = (right+left)/2
#print(midle)


while (a!=True):
    if (left==right):
        a=True
        print("Ваше число равно: " + str(left) + "? Да/Нет")
        if ("Да" in input()):
            break
    if (midle%int(midle)==0):
        print("Ваше число равно: " + str(midle) + "? Да/Нет")
        if ("Да" in input()):
            a=True
            print("Ваше число: " + str(midle))
            break

    print("Ваше число меньше " + str(midle) +"? Да/Нет")
    if ("Да" in input()):
        right = math.floor(midle)
        midle = (right+left)/2
    else:
        left = math.ceil(midle)
        midle = (right+left)/2



    
     

#midle=(right-left+1)/2
