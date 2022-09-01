# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, 
# знаменатель которых не превышает 11.

for i in range(1, 11):
    for j in range(i+1, 12):
        if i == 1:
            print (f'{i}/{j}')
        else:
            logic = True
            for k in range(2, i+1):
                if i%k == 0 and j%k ==0:
                    logic = False
            if logic == True: 
                print (f'{i}/{j}')