# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN. 
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

N = input("Введите натуральное число: ")

# N = '132'
print(N)
Sum = 0
count = 1
while count < 4:
    Sum += int(N*count)
    count +=1
print(Sum)