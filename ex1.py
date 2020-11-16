x = int(input("Введите количество километров: "))
y = int(input("Введите число: "))
day = 1
while x < y:
    x *= 1.1
    day += 1
print(day)

