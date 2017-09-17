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
def orangecap(match_score):
    player_score={}
    for i in match_score.keys():
        for j in match_score[i].keys():
            try:
				player_score[j.capitalize()]= player_score[j.capitalize()]+match_score[i][j]
            except KeyError:
                player_score[j.capitalize()]= match_score[i][j]
    maximum = -1
    for i in player_score.keys():
        if player_score[i]>maximum:
            maximum = player_score[i]
            maxname = i
    return (maxname,maximum)


def main():
    pass

if __name__ == '__main__':
    main()
example1 = {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
example2 = {'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}}
print orangecap(example1)
print orangecap(example2)

