#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     19-03-2017
# Copyright:   (c) DELL 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10000000)
def fibonacci(n):
    try:
        if fibtable[n]:
            return fibtable[n]
    except KeyError:
        pass
    if n==0 or n==1:
        value = n
    else:
        value = fibonacci(n-1)+fibonacci(n-2)
    fibtable[n]=value
    return value

def main():
    pass

if __name__ == '__main__':
    main()
fibtable = {}
n = int(raw_input())
print fibonacci(n)