# # 2. Вычислить факториал введённого числа.
# chislo = int(input("Введите число: "))
# factorial = 1
#
# while chislo > 1:
#     factorial = factorial * chislo
#     chislo -= 1
# print("Факториал введеного числа, равен:", factorial)

# 1. Вывести на экран столько элементов ряда Фибоначчи, сколько указал пользователь.
# Например, если на ввод поступило число 6, то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 2 3 5 8 13.

UsInput = int(input("Введите число: "))
fib1 = fib2 = 1
while UsInput >= 1:
    fib = fib1
    fib1 = fib2
    fib2 = fib + fib1
    print(fib1, end=" ")
    UsInput -=1