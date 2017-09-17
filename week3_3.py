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
def matmult(l1,l2):
    (m,n,p)=(len(l1),len(l2),len(l2[0]))
    matrix = [[0 for x in range(p)]for y in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                matrix[i][j]=matrix[i][j]+l1[i][k]*l2[k][j]
    return matrix

def print_matrix(l):
    for i in range(len(l)):
        print " ".join(map(str,l[i]))

if __name__ == '__main__':
    main()
(l1,l2)=([],[])

n=raw_input()
while True:
    if n=="":
        break
    l1.append(list(map(int,n.split(" "))))
    n=raw_input()
    
    
n=raw_input()
while True:
    if n=="":
        break
    l2.append(list(map(int,n.split(" "))))
    n=raw_input()
print_matrix(matmult(l1,l2))
