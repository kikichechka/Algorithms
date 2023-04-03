n = 50
summa = 0
for i in range(1, n+1):
    summa += i

print(summa)

# Написать алгоритм поиска простых чисел (делятся только на себя и
# на 1) в диапазоне от 1 до N

n = 50
flag = True
for i in range(1, n + 1):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = False
            break

    if flag:
        print(i, end = ' ')
    flag = True


    for i in 0, 1, 2, 3:
        for j in 0, 1, 2, 3:
            for k in 0, 1, 2, 3:
                for m in 0, 1, 2, 3:
                    print(i, j, k, m)


#Фибоначи рекурсия и цикл
import datetime

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_for(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        x = fib1 + fib2
        fib1 = fib2
        fib2 = x
    return fib1




n = 40
start_time = datetime.datetime.now()
print(fib(n))
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
print(fib_for(n))
end_time = datetime.datetime.now()
print(end_time - start_time)
