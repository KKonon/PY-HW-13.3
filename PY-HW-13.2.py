# 2. Вычислить факториал введённого числа.
chislo = int(input("Введите число: "))
factorial = 1

while chislo > 1:
    factorial = factorial * chislo
    chislo -= 1
print("Факториал введеного числа, равен:", factorial)