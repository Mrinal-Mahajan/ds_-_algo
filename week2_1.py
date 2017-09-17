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
def main():
    pass
def interverse(n):
    ans = 0
    while n>0:
        ans = ans*10 + n%10
        n= n//10
    return ans
if __name__ == '__main__':
    main()
print interverse(input()) 