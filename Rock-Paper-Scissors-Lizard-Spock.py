import random


rock = '✊'
paper = '✋'
scissor = '✌️'
spock = '🖖'
lizard = '🦎'
loop = 1

while loop == 1:
    print('================================\nRock Paper Scissors Lizard Spock\n================================') #introduction
    print(f'1) {rock}')
    print(f'2) {paper}')
    print(f'3) {scissor}')
    print(f'4) {lizard}')
    print(f'5) {spock}')

    player = int(input('Pick a number: ')) # input of player
    computer = random.randint(1, 5) # random choiche of cpu

    print('')

    print(f'Your choose: {player}') #result player
    print(f'CPU choose: {computer}') #result cpu

    #         PLAYER WON            
    if player == 1 and computer == 3 :
        print('The player won!🙋')
    elif player == 3 and computer == 2 :
        print('The Player won!🙋')
    elif player == 2 and computer == 1 :
        print('The player won!🙋')
    elif player == 1 and computer == 4 :
        print('The player won!🙋')
    elif player == 4 and computer == 5 :
        print('The player won!🙋')
    elif player == 5 and computer == 3 :
        print('The player won!🙋')
    elif player == 3 and computer == 4 :
        print('The player won!🙋')
    elif player == 4 and computer == 2 :
        print('The player won!🙋')
    elif player == 2 and computer == 5 :
        print('The player won!🙋')
    elif player == 5 and computer == 1 :
        print('The player won!🙋')
    #         CPU WON
    elif computer == 1 and player == 3 :
        print('The CPU won!💻')
    elif computer == 3 and player == 2 :
        print('The CPU won!💻')
    elif computer == 2 and player == 1 :
        print('The CPU won!💻')
    elif computer == 1 and player == 4 :
        print('The CPU won!💻')
    elif computer == 4 and player == 5 :
        print('The CPU won!💻')
    elif computer == 5 and player == 3 :
        print('The CPU won!💻')
    elif computer == 3 and player == 4 :
        print('The CPU won!💻')
    elif computer == 4 and player == 2 :
        print('The CPU won!💻')
    elif computer == 2 and player == 5 :
        print('The CPU won!💻')
    elif computer == 5 and player == 1 :
        print('The CPU won!💻')
    #         DRAW
    elif player == 1 and computer == 1 :
        print('Draw🥱')
    elif player == 2 and computer == 2 :
        print('Draw🥱')
    elif player == 3 and computer == 3 :
        print('Draw🥱')
    elif player == 4 and computer == 4 :
        print('Draw🥱')
    elif player == 5 and computer == 5 :
        print('Draw🥱')
    #         INPUT ERROR
    else:
        print('Input error')
