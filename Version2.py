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
import Encryptor as ep

q = ord('A')
def encypt():
    my_file = open(read, "r")
    my_write =  open(write, "w")
    for i in my_file:
        count = 0
        if(len(i)%2 == 1):
            i+="\0"
        for j in range(len(i)):
            if( count %2 == 1):
                # print(i[j])
                l = ord(i[j])
                o = k*256 + l
                if(debug):
                    print(chr(k),chr(l),bin(o))
                p = ep.encrypt(o)
                strng = str(p) + "-"
                my_write.write(strng)
            k = ord(i[j])
            count +=1
    print("Done Encrypting")
    my_file.close()
    my_write.close()

def unread(num):
    num2 = num%256
    num1 = int(num/256)
    return(num1,num2)

def decrypt():
    strng = ""
    fnl = ""
    my_decr =  open("output.txt", "r")
    for i in my_decr:
        for j in i:
            if(j != "-"):
                strng += j
            else:
                x1,x2 = unread(ep.fast_dec(int(strng)))
                fnl1 = chr(x1)+chr(x2)
                fnl+= fnl1
                # fnl+=chr(ep.fast_dec(int(strng)))
                strng = ""
    print(fnl)
    my_decr.close()

if __name__ == '__main__':
    if(mode == 'e'):
        print("Encryption Start")
        encypt()
    elif(mode == 'd'):
        decrypt()
    else:
        print("Error, Please try again")