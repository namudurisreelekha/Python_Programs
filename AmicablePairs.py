def divisors(num):
    sum = 0
    for i in range(1,num):
        if (num%i == 0):
            sum+=i
    return sum
k=[]
l = [divisors(i) for i in range(10000)]
for i in range(1,10000):
    if (l[i]<10000) and (i<l[i]) and (l[i] >=1) and(l[l[i]]==i):
        k.append(i)
        k.append(l[i])
print(sum(k))
