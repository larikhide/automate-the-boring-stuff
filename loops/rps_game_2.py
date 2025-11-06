import random, sys

print('ROCK', 'PAPER', 'SCISSORS')

wins, loses, ties = 0, 0, 0
while True:
    print('%s Wins, %s Loses, %s Ties' % (wins, loses, ties))
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')

    while True:
        move = input('>')

        if move == 'q':
            sys.exit()
        if move == 'r' or move == 'p' or move == 's':
            break
        print('Type one of r, p, s or q')

    if move == 'r':
        print('ROCK versus...')
    elif move == 'p':
        print('PAPER versus...')
    elif move == 's':
        print('SCISSORS versus...')

    computer_move = random.randint(1, 3)
    if computer_move == 1:
        computer_move = 'r'
        print('ROCK')
    elif computer_move == 2:
        computer_move = 'p'
        print('PAPER')
    elif computer_move == 3:
        computer_move = 's'
        print('SCISSORS')

    if move == computer_move:
        ties+=1
        print('It is a tie!')
    elif move == 'r' and computer_move == 's' or move == 'p' and computer_move == 'r' or move == 's' and computer_move == 'p':
        wins+=1
        print('It is a win!')
    else:
        loses+=1
        print('It is a lose!')

