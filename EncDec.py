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

'''
5570731 4123220 3140362 6576891 4123220 5599982 1207644 5682468 6062308 1207644 2618231 2618231 1207644 480745 3140362 6576891 2105919 31271 1207644 2618231 5088577 2618231 313858 6003217 6003217 100792 5682468 5599982 31271 6062308 2090845 1207644 2618231 2618231 1207644 480745 3140362 6576891 2105919 31271 1207644 4194425 1731899 6439243 2090845 6062308 4592324 6003217 4420608 31271 3140362 6576891 4592324 3140362 2393966 2090845 1207644 2618231 2618231 1207644 480745 3140362 6576891 2105919 31271 1207644 100792 533017 5599982 5599982 2090845 3140362 6062308 1207644 5570731 31271 533017 4826769 4826769 6439243 1731899 6412614 2618231 839417 6003217 
'''