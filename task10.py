
import time
summator = 0
x = 2000000


def is_simple(number):
    d = 2
    while d**2 <= number and number % d != 0:
        d += 1
    return d**2 > number


for i in range(2, x):
    if is_simple(i)==True:
        summator += i



print("Result is {0}".format(summator))



