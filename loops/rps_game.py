import random
print('ROCK, PAPER, SCISSORS')

wins, loses, ties = 0, 0, 0
while True:
    print(wins, 'Wins,', loses, 'Loses,', ties, 'Ties')
    print('Enter your move: (r)ock, (p)aper, (s)cissors and (q)uit')

    move = input('>')
    if move == 'p':
        print('PAPER versus...')
    elif move == 'r':
        print('ROCK versus...')
    elif move == 's':
        print('SCISSORS versus...')
    elif move == 'q':
        break
    else:
        print('Please enter r, p, s or q')
        continue

    versus = random.randint(1, 3)
    if versus == 1:
        versus = 'r'
        print('ROCK')
    elif versus == 2:
        versus = 'p'
        print('PAPER')
    else:
        versus = 's'
        print('SCISSORS')

    if move == versus:
        print('It is a tie!')
        ties=ties+1
    elif move == 'r' and versus == 's' or move == 'p' and versus == 'r' or move == 's' and versus == 'p':
        print('It is a win!')
        wins=wins+1
    elif (move == 'p' and versus == 's') or (move == 'r' and versus == 'p') or (move == 's' and versus == 'r'):
        print('It is a lose!')
        loses=loses+1

