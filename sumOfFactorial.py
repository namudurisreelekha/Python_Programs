fact=1
for i in range(1,101):
    fact = fact*i
strnum = list(str(fact))
total = sum([int(j) for j in strnum])
print(total)
