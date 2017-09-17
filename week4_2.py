#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     13-03-2017
# Copyright:   (c) DELL 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def addpoly(p1,p2):
    p3 = []
    (m,n,i,j) = (len(p1),len(p2),0,0)
    while i<m and j<n:
        if p1[i][1]>p2[j][1]:
            p3.append(p1[i])
            i=i+1
        elif p1[i][1]<p2[j][1]:
            p3.append(p2[j])
            j=j+1
        elif p1[i][1]==p2[j][1]:
            sum = p1[i][0]+p2[j][0]
            if sum != 0:
                p3.append((sum,p1[i][1]))
            (i,j)=(i+1,j+1)
    if j<n:
        p3 = p3 + p2[j:]
    elif i<m:
        p3 = p3 +p1[i:]
    return p3
def multpoly(p1,p2):
    p3=[]
    temp = {}
    (m,n)=(len(p1),len(p2))
    for i in range(m):
        for j in range(n):
            try:
                temp[p1[i][1]+p2[j][1]]=temp[p1[i][1]+p2[j][1]]+p1[i][0]*p2[j][0]
            except KeyError:
                temp[p1[i][1]+p2[j][1]]=p1[i][0]*p2[j][0]
    for i in sorted(list(temp.keys())):
        if temp[i] != 0:
            p3.append((temp[i],i))
    p3.reverse()
    return p3
def main():
    pass

if __name__ == '__main__':
    main()
print addpoly([(2,1)],[(-2,1)])
print addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
print multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
print multpoly([(4,3),(3,0)],[(-4,3),(2,1)])