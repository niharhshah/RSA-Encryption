import Encryptor
debug = 0
for i in range(4567):
    p = Encryptor.encrypt(i)
    q = Encryptor.fast_dec(p)
    if(debug):
        print("p =",p,"\t" ,"q = ",q)
    if(i != q):
        print("Failed")
        raise FailedError("Try Debugging")
print("Passed")