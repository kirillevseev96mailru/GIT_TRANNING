import random
import math
import time


def counter(s1, s2):
    t = 1
    count = 0
    while t == 1:
        if s1.find(s2) > -1:
            count = count + 1
            index = s1.find(s2)
            pos = index + len(s2)
            s1 = s1[pos:]
        else:
            t = 0
    return count


s1 = 'FAFFAFFAFDFSFGAGFADGVNDCNDHFFA'
s2 = 'FA'
#print(counter(s1, s2))


def sum_numbers_1(s1, s2):
    sum_nums = 0
    for i in range(len(s1)):
        sum_nums = sum_nums + int(s1[i])
    for i in range(len(s2)):
        sum_nums = sum_nums + int(s2[i])
    return(sum_nums)


#n = float(input('Введите вещественное число: '))
#n = str(n)
#s1, s2 = n.split('.')
#print(sum_numbers_1(s1,s2))


 # def random_generator(N, fnum, lnum):
 #   -3 -2 -1 0 1 2 3


def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(10000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


def random_generator(N, fnum, lnum):
    result = []
    my_array = []
    for i in make_pi():
        my_array.append(i)
    my_array = my_array[1:]
    j = 0
    while j != N:
        j += 1
        random_num = round(my_array[1] * 2 * 11 * math.pi * time.localtime().tm_sec)
        my_array = my_array[1:]
        num = 0
        k = 0
        while k != random_num:
             for i in range(fnum, lnum):
                 num = i
                 k = k + 1
                 if k == random_num:
                     break

        result.append(num)

    print(result)


random_generator(1, -93, 45)
