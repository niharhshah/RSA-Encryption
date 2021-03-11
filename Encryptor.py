import math
#convert to integer
p = 1097 
q = 6353
n = p*q 
z = (p-1)*(q-1)
e = 585
d = 23801
def encrypt(m):
    cypher = (m**e) % n
    return cypher
def decry(c):
    msg = (c**d)%n
    return msg

def fast_dec(c):
    temp = 1
    for power in range(d):
        # print(temp,c,d,power)
        temp = (temp*c)%n
    return temp

if __name__ == '__main__':
    if(math.gcd(e,z) == 1 and ((e*d)%z) == 1):
        print(((e*d)%z))
        print("OK GO AHEAD")
        print(p,q,e,d,z,n)
        print(ord('A'))
        p = encrypt(65)
        print(p)
        print(decry(p))#(encrypt(ord('A'))))
