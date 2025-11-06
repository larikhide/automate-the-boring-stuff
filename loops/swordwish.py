while True:
    print('Who are you?')
    name = input('>')

    if name != 'Joe':
        continue
    else:
        print('Enter your password')
        password = input('>')
        if password == 'swordwish':
            break
print('Access granted')

