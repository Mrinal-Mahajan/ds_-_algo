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
def is_alternating(l):
    for i in range(1,len(l)-1):
        if l[i]>=l[i-1] and l[i]<=l[i+1]:
            return False
        elif l[i]<=l[i-1] and l[i]>=l[i+1]:
            return False
    return True

if __name__ == '__main__':
    main()
(list1,n)=([],0)
n=raw_input()
while True:
    if n=="":
        break
    list1.append(int(n))
    n=raw_input()
print is_alternating(list1)