import os

site = input("Введите название сайта: ")
again = False
dot = ""

while again!= True:
    if "https://" in site:
        if "www." in site:
            if ".com" or ".ru" in site:
                os.system("start" + site)
                #print("if")

    elif "www." in site:
        if ".com" or ".ru" in site:
            os.system("start https://" + site)
            #print("elif 1")

    elif (".com" or ".ru") in site:
        os.system("start https://www." + site)
        #print("elif 2")

    else:
        dot = input("Ваш сайт заканчивается на ru или com или другое окончание? (ru/com/Указать без точки)\n") 
        if dot == "ru":
            os.system("start https://www." + site + ".ru")
        elif dot == "com":
            os.system("start https://www." + site + ".com")
        else:
            os.system("start https://www." + site + "." +dot)
    print("Желаете открыть другой сайт? (Да/Нет)")
    if input() == "Нет":
        again = True
        print("Удачного вам сёрфинга в интернете!")
    else:
        site = input("Введите название сайта: ")
        dot = ""
    