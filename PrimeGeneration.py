import math
import random

prime = []

for tstPrime in range(100000,1000000):
    # print(tstPrime)
    flg = 0
    for i in range(2,int(math.sqrt(tstPrime))+1):
        if(tstPrime % i == 0):
            flg = 1
            break
    if(flg == 0):
        prime.append(tstPrime) 

p,q = [random.choice(prime),random.choice(prime)]
n = p*q
print(p,q,n)