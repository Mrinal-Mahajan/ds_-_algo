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
def lcw(u,v):
    lcw = [[0 for i in range(len(v)+1)]for j in range(len(u)+1)]
    maxLCW = 0
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r]==v[c]:
                lcw[r][c]=1+lcw[r+1][c+1]
            else:
                lcw[r][c]=0
            if lcw[r][c]>maxLCW:
                maxLCW = lcw[r][c]
                i = r
    return (maxLCW,i)

def lcs(u,v):
    lcs = [[0 for i in range(len(v)+1)]for j in range(len(u)+1)]
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r]==v[c]:
                lcs[r][c]=1+lcs[r+1][c+1]
            else:
                lcs[r][c]=max(lcs[r+1][c],lcs[r][c+1])
    return lcs[0][0]


def main():
    pass

if __name__ == '__main__':
    main()
(u,v)=map(str,raw_input().split(" "))
(length,start) = lcw(u,v)
print u[start:start+length]
print lcs(u,v)