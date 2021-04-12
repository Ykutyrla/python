"""Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d."""

#список
mas = [3, 7, 4]
#предположим,что первый элемент максимальный
maximum = mas[0]
for i in range (1, len(mas)):
    if mas[i]>maximum:
        maximum=mas[i]
print (maximum)

