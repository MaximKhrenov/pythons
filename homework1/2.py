side1 = int(input("Введите 1значение"))
side2 = int(input("Введите 2значение"))
sugn = input("Введите + ИЛИ - ")

if sugn == "-":
    print(side1 - side2)
elif sugn == "+":
    print(side1 + side2)
elif sugn != side2 or side2:
    print("Корректно введите символ")
