n=int(input())
lw=n
k = n

while lw!=0:
    if(lw==1):
        print("factorial: {0}".format(k))
        break
    k *= (lw - 1)
    lw-=1

mas =[]
m = k
count=0
while (m>1):
    m/=10
    count+=1

sum =0
for i in range(count):
    mas.append(k % 10)
    sum+=mas[i]
    k//=10


print ("sum of numbers: {0}".format(sum))


