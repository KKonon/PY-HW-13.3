# Найти все числа, кратные 11, в диапазоне от 0 до 10000.

chislo = 11;

for i in range(0,10001):
    if i == 0:
       continue

    if i % chislo == 0:
        print(i)