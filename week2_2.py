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
def bracket_match(str):
    ans=0
    for i in range(0,len(str)):
        if ans<0:
            return False
        else:
            if str[i]=='(':
                ans = ans+1
            elif str[i]==')':
                ans = ans-1
    return ans==0
if __name__ == '__main__':
    main()
print bracket_match(raw_input())