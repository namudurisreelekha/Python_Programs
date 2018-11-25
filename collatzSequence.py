def collatz_seq (n):
    chainNumber = 1
    n1 = n
    while n1 != 1:
        if n1 % 2 == 0:
            n1 = n1/2
            length += 1
        else:
            n1 = (3*n1) + 1
            length += 1
    return [length, n]

fullList = []
for i in range(2, 1000000):
    fullList.append(collatz_seq(i))
sortedList = sorted(fullList, reverse=True)
print(sortedList[:1])
