
#need to optimize
def fibonach(x):
    if (x==1):
        return 1
    if(x==2):
        return 1
    if(x>2):
        return fibonach(x-1)+fibonach(x-2)

def number_checker(number):
    counter = 0
    number_quantity = number
    while (number_quantity >= 1):
        number_quantity /= 10
        counter += 1
    return counter

result =0
iterator = 1
while(number_checker(result)!=5):
    if (number_checker(result<5)):
        iterator+=900
    else:
        iterator += 1
    result = fibonach(iterator)


print(result)


