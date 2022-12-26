# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
import random
os.system('cls')

k = int(input('Enter degree K: '))

my_list = []
for _ in range(k+1):
    my_list.append(random.randint(0, 101))
print('List of coefficients:', my_list)

with open('polynomial.txt', 'w') as data:
    for i in range(k+1):
        if my_list[i]==0:
            continue
        elif (k-i)==1:
            data.write(f' {my_list[i]*1}x +')
        elif (k-i)==0:
            data.write(f' {my_list[i]*1}')
        else:
            data.write(f' {my_list[i]}x^{k-i} +')
    data.write(' = 0')
