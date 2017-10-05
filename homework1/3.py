value = int(input("Введите число"))
list = []
for i in range(2, value+1):
    for q in list:
        if i % q == 0:
            break
    else:
        list.append(i)
print(list)

