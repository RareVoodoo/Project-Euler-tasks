
a =2**1000
k = a


def number_quantity(number):
    counter = 0
    while(number >= 1):
        number/=10
        counter+=1
    return counter


def summator(number,range_arr):
    sum = 0
    array = []
    for i in range(range_arr):
        array.append(number%10)
        sum += array[i]
        number//=10

    return sum

print(summator(k,number_quantity(a)))
