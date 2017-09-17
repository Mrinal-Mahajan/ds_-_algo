#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     14-03-2017
# Copyright:   (c) DELL 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def player_sort(l,left,right):
    if right-left <=1:
        return
    yellow = left+1
    for green in range(left+1,right):
        x=1
        while l[green][x]==l[left][x]:
            x = x+1
        if x<=4:
            if l[green][x]>l[left][x]:
                (l[green],l[yellow])=(l[yellow],l[green])
                yellow = yellow+1
        else:
            if l[green][x]<l[left][x]:
                (l[green],l[yellow])=(l[yellow],l[green])
                yellow = yellow+1
    (l[left],l[yellow-1])=(l[yellow-1],l[left])
    player_sort(l,left,yellow-1)
    player_sort(l,yellow,right)

def total(l):
    sum =0
    for i in range(len(l)):
        sum = sum + l[i]
    return sum
def sets_won(l1,l2):
    (i,j) = (0,0)
    for x in range(len(l1)):
        if l1[x]>l2[x]:
            i = i+1
        else:
            j = j+1

    return (i,j)

def main():
    pass

if __name__ == '__main__':
    main()
player_stat = {}
while True:
    string = raw_input()
    if string=="":
        break
    data = string.strip().split(':')
    score = data[2].split(',')
    (l1,l2)=([],[])
    for q in range(len(score)):
        sets = score[q].split('-')
        l1.append(int(sets[0]))
        l2.append(int(sets[1]))
    for player in [data[0],data[1]]:
        try:
            player_stat[player]
        except KeyError:
            player_stat[player] = [0,0,0,0,0,0]

    (i,j) = sets_won(l1,l2)
    (total1,total2) = (total(l1),total(l2))
    if len(score)<=3:
        if abs(i-j)<=2:
            x=1
        else:
            x=0
    else:
        x=0

    player_stat[data[0]][x] = player_stat[data[0]][x]+1
    player_stat[data[0]][2] = player_stat[data[0]][2]+i
    player_stat[data[0]][3] = player_stat[data[0]][3]+total1
    player_stat[data[0]][4] = player_stat[data[0]][4]+j
    player_stat[data[0]][5] = player_stat[data[0]][5]+total2

    player_stat[data[1]][2] = player_stat[data[1]][2]+j
    player_stat[data[1]][3] = player_stat[data[1]][3]+total2
    player_stat[data[1]][4] = player_stat[data[1]][4]+i
    player_stat[data[1]][5] = player_stat[data[1]][5]+total1

    print player_stat
temp_list = []
for i in player_stat.keys():
    temp_list.append([i]+player_stat[i])
player_sort(temp_list,0,len(temp_list))
for i in range(len(temp_list)):
    for j in range(7):
        print temp_list[i][j]," ",
    print ""











