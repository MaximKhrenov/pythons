num1 = int(input('Введите 1 число'))
num2 = int(input('Введите 2 число'))

list=[]

for i in range(num1, num2+1):
    if i%5 ==0:
        list.append(i)


print(list)
