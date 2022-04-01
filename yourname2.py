while True:
    print('Please type your name.')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
            break
print('Thank you!')    