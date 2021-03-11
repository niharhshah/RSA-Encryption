import Encryptor as ep
'''
mode:
    0 Enc
    1 Dec
'''
mode = 1

debug = 0




def encypt():
    my_file = open("planetext.txt", "r")
    my_write =  open("encoded.txt", "w")
    for i in my_file:
        for j in i:
            p=ep.encrypt(ord(j))
            strng = str(p) + " "
            my_write.write(strng)
            if(debug):
                print(p,j)
    print("Done Encrypting")
    my_file.close()
    my_write.close()

def decrypt():
    strng = ""
    fnl = ""
    my_decr =  open("encoded.txt", "r")
    for i in my_decr:
        for j in i:
            if(j != " "):
                strng += j
            else:
                fnl+=chr(ep.fast_dec(int(strng)))
                strng = ""
    print(fnl)
    my_decr.close()

if __name__ == '__main__':
    if(mode == 0):
        encypt()
    else:
        decrypt()
