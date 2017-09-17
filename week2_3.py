#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     12-03-2017
# Copyright:   (c) DELL 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    pass
def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                return False
    return True

if __name__ == '__main__':
    main()
list1=[]
n=raw_input()
while True:
    if n=="":
        break
    else:
        list1.append(int(n))
        n=raw_input()

print sum(filter(lambda x:isprime(x),list1))
