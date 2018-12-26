import time

timer1 = time.time()
def triangle_numbers(n):
    if n==1:
        return 1
    if n==101:
        return 5151
    if n==1000:
        return 500500
    if n==1997:
       return 1995003
    else:
        return n + triangle_numbers(n-1)

devider = 500
i=1

div_count = 0
hold_var = 0
while(div_count < devider):
   triag = triangle_numbers(i)
   print(i)
   for j in range(1, triag+1):
       if triag % j ==0:
           div_count += 1
   if div_count < devider:
        div_count=0
        i+=1

timer2 = time.time()

print(triag)
print("{0} seconds".format(timer2-timer1))