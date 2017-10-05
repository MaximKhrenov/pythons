count_points = 0

while (True):
    task1 = input('Что лучше PHP или Python')
    if (task1  == 'Python' or task1 == 'python' or task1  == 'PYTHON' or task1  == 'питон' or task1  == 'Питон' or task1  == 'Пайтон' ):
        count_points += 1
        print('Правильно!')
    else:
        print('PHP привет динозаврам')

    task2 = input('Функция для измерения длины строки ')
    if ( task2 == 'Len' or task2 == 'len'):
        count_points += 1
        count_len = len(task2)
        print('Правильно! и длина введенного тобой значения:', count_len)
    else:
        print('Неа')

    task3 = input('Какая функция возвращающий список строки?')
    method_split = task3.split()
    if (task3 == 'split' or task3 == 'split'):
        count_points += 1
        print('Правильно это', method_split )
    else:
        print('Неа')

    task4 = input('True это? ')
    if (task4 == '1'):
        count_points += 1
        print('Правильно это 1!')
    else:
        print('Неа')

    task5 = input('False это?')
    if (task5 == '0'):
        count_points += 1
        print('Правильно это 0!')
    else:
        print('Неа')

    task6 = input('Как обозначается функция в python?')
    if (task6 == 'Def' or task6 == 'def'):
        count_points += 1
        print('Правильно!')
    else:
        print('Неа:')

    task7 = input('Какой отступ нужно backspace соблюдать в Python?')
    if (task7 == '4' or task7 == 'четыре'):
        count_points += 1
        print('Правильно!')
    else:
        print('Неа')

    task8 = input('Число с плавающей точкой в Python?')
    if (task8 == 'float' or task8 == 'Float'):
        count_points += 1
        print('Правильно!')
    else:
        print('Неа')

    task9 = input('Какая функция для ввода текста в Python?')
    if (task9 == 'input' or task9 == 'Input'):
        count_points += 1
        print('Правильно')
    else:
        print('Неа')

    task10 = input('И на поседок, как зовут преподавтеля?')
    if (task10 == 'Никита Соболев' or task10 == 'Соболев Никита' or task10 == 'соболев никита'):
        count_points += 1
        print('Правильно!')
    else:
        print('Неа')

    replace = input("Повторить тест?")
    if (replace == 'да' or replace == 'Да'):
        continue
    elif (replace == 'Нет' or replace == 'нет'):
        print('Количество праивльных ответов: ', count_points)
        print("Спасибо за пройденный тест!")
        break