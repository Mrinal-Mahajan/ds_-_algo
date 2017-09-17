#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     18-03-2017
# Copyright:   (c) DELL 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()
(m,n)=(int(input("Enter no. of rows: ")),int(input("Enter no. of columns: ")))
while True:
    (sx,sy)=(int(input("Enter starting row of knight: ")),int(input("Enter starting column of knight: ")))
    if(sx<m and sx>=0) and (sy<n and sy>=0):
        break
    else:
        print "Your input is not valid , try again"
while True:
    (tx,ty)=(int(input("Enter target row of knight: ")),int(input("Enter target column of knight: ")))
    if(tx<m and tx>=0) and (ty<n and ty>=0):
        break
    else:
        print "Your input is not valid , try again"

level = [[-1 for i in range(n)]for j in range(m)]
parent = [[0 for i in range(n)]for j in range(m)]
level[sx][sy]=0
queue = [(sx,sy)]
while queue != []:
    if level[tx][ty]!=-1:
        break
    (i,j) = queue.pop(0)
    for row in [-2,2]:
        for col in [-1,1]:
            try:
                if level[i+row][j+col]==-1 and i+row<m and i+row>=0 and j+col<n and j+col>=0:
                    level[i+row][j+col]=level[i][j]+1
                    parent[i+row][j+col] = (i,j)
                    queue.append((i+row,j+col))
            except IndexError:
                pass
    for row in [-1,1]:
        for col in [-2,2]:
            try:
                if level[i+row][j+col]==-1 and i+row<m and i+row>=0 and j+col<n and j+col>=0:
                    level[i+row][j+col]=level[i][j]+1
                    parent[i+row][j+col] = (i,j)
                    queue.append((i+row,j+col))
            except IndexError:
                pass

if level[tx][ty] != -1:
    print "Yes, it's reachable"
    print "No. of steps required to reach: {}".format(level[tx][ty])
    l = []
    point = (tx,ty)
    l.append(point)
    while point!= (sx,sy):
    	point = parent[point[0]][point[1]]
    	l.append(point)
    print "The shortest path is: " + "->".join(map(str,l[::-1])) 
else:
    print "Sorry knight can't reach the target"



