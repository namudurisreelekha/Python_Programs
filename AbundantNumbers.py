def divisors(num):
    tot = 0
    for i in range(1,num):
        if (num%i == 0):
            tot+=i
    return tot<num

        
