list_to_keep = []
while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    else:
        list_to_keep.append(number)
print("Выводим введённые числа: ", list_to_keep)

print("Количество введённых чисел: ", len(list_to_keep))

def summa(list_to_keep):
    thesumma = 0
    for i in list_to_keep:
        thesumma += i
    return thesumma
print("Сумма введённых чисел: ", summa(list_to_keep))

def multiply(list_to_keep):
    themulti = 1
    for i in list_to_keep:
        themulti *= i
    return themulti
print("Произведение введённых чисел: ", multiply(list_to_keep))

def average(list_to_keep):
    return sum(list_to_keep) / len(list_to_keep)
print("Среднее арифметическое введённых чисел: ", average(list_to_keep))

def max(list_to_keep):
    index_of_max = 0
    for i in list_to_keep:
        if i > index_of_max:
            index_of_max = i
    return(index_of_max)
print("Выводим значение и порядковый номер наибольшего элемента последовательности: ",
max(list_to_keep),   list_to_keep.index(max(list_to_keep)) + 1)

def evenodd(list_to_keep):
    even = 0
    odd = 0
    for i in list_to_keep:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
print("Выводим количество чётных и нечётных элементов в последовательности: ", evenodd(list_to_keep))

def secondmax(list_to_keep):
    max_digit = 0
    second_max_digit = 0
    for value in sorted(list_to_keep):
        if second_max_digit < value:
            second_max_digit = max_digit
        if max_digit < value:
            max_digit = value
    return second_max_digit
print("Выводим значение второго по величине элемента в этой последовательности: ", secondmax(list_to_keep))

print("Выводим сколько элементов этой последовательности равны ее наибольшему элементу: ",
list_to_keep.count(max(list_to_keep)))

