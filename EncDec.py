import Encryptor as ep
import sys
args = sys.argv
'''
mode:
    0 Enc
    1 Dec
'''
if(len(args)< 4):
    args.append(".TestFile")
mode = args[1]
read = args[2]
write = args[3]
debug = 0




def encypt():
    my_file = open(read, "r")
    my_write =  open(write, "w")
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
    my_decr =  open(read, "r")
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
    if(mode == 'e'):
        encypt()
    elif(mode == 'd'):
        decrypt()
    else:
        print("failed Please try again")

