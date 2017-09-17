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
def is_descending(l):
    for i in range(1,len(l)):
        if l[i]>l[i-1]:
            return False
    return True
if __name__ == '__main__':
    main()
(list1,n)=([],raw_input())
while True:
    if n=="":
        break
    else:
        list1.append(int(n))
        n=raw_input()
print is_descending(list1)
