import random
import winsound
from time import sleep

ch,scoreu,scorecomp='y',0,0
while ch in ['y','yes','ya']:
    winsound.Beep(2500,300)
    u_in=input('\nenter your move:').lower()
    comp=random.randint(1,3)
    #[rock,paper,scissor]=[1,2,3]
    if u_in=='rock':
        if comp==1:
            print('tie')
        elif comp==2:
            print('1 for computer')
            scorecomp+=1
        elif comp==3:
            print('1 for you!')
            scoreu+=1
    elif u_in == 'paper':
        if comp == 2:
            print('tie')
        elif comp == 3:
            print('1 for computer')
            scorecomp += 1
        elif comp == 1:
            print('1 for you!')
            scoreu += 1
    elif u_in == 'scissor':
        if comp == 3:
            print('tie')
        elif comp == 1:
            print('1 for computer')
            scorecomp += 1
        elif comp == 2:
            print('1 for you!')
            scoreu += 1
    else:
        print('\nDONT ACT SMART ;-)')
    
    if scorecomp>=5 or scoreu>=5:
        print('\n --------------------------------------------------------------------RESULT-------------------------------------------------------\n')
        for i in range(4):
            winsound.Beep(1500,250)
            sleep(0.1)
        if scorecomp>scoreu:
            print('\nComputer WON')
        else:
            print('\nYOU WON!!')
        print('\nCOMPUTER: {0} \nYOU: {1}'.format(scorecomp,scoreu))
        ch=input('\nWould you like to continue?:').lower()
        scorecomp,scoreu=0,0
