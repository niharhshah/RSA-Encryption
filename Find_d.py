import random
import math
my_p = 1097
my_q = 6353
def find_d(expe,p,q):
    z = (p-1)*(q-1)
    n = p*q
    d=0.0
    darr=[]
    print(z)
    for i in range(1,n):
        for e in expe:
            # print(type(e),type(i))
            if((e*i)%z == 1):
                print((e*i)%z)
                return i,e
        # # d = (i*z  +1)/e
        # if(d - int(d) == 0):
        #     d = int(d)
        #     if(((e*d)%z) == 1):
        #         darr.append(d)
    return darr#random.choice(darr)
def find_e(p,q):
    n = p*q
    z = (p-1)*(q-1)
    # print(z)
    earr = []
    for i in range(2,1000):
        if(math.gcd(i,z) == 1):
            earr.append(i)
    return earr            
if __name__ == '__main__':
    # print(find_e(my_p,my_q))
    my_e = (find_e(my_p,my_q))
    print(find_d(my_e,my_p,my_q))