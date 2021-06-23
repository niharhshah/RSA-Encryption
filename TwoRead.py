my_file = open("planetext.txt", "r")
my_write =  open("output.txt", "w")
def twoRead():
    for i in my_file:
        count = 0
        if(len(i)%2 == 1):
            i+="\0"
        for j in range(len(i)):
            if( count %2 == 1):
                # print(i[j])
                l = ord(i[j])
                o = k*256 + l
                print(chr(k),chr(l),(o))
                # count = 0
            k = ord(i[j])
            count +=1
def unread(num):
    num2 = num%256
    num1 = int(num/256)
    print(chr(num1),chr(num2))
if __name__ == '__main__':
    twoRead()
    unread(12594)