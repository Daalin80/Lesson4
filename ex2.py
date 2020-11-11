list_to_keep = []
while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    else:
        list_to_keep.append(number)
print("Выводим введённые числа: ", list_to_keep)

print("Количество введённых чисел: ", len(list_to_keep))

def Summa(list_to_keep):
    thesumma = 0
    for i in list_to_keep:
        thesumma = thesumma + i
        return thesumma
print(Summa(list_to_keep))




