print('''
You enter a room with two doors. \n
Do you go through door #1 or door #2?
''')

door = input('> ')

if door == '1':
    print('There\'s a giant bear here eating a cheesecake.')
    print('What do you do?')
    print('#1 take the cake.')
    print('#2 scream like a banshee.')

    bear = input('> ')

    if bear == '1':
        print('The bear eats your face off.')
    elif bear == '2':
        print('The bear eats your still pumping heart.')
    else:
        print(f'Well, doing {bear} is probably better.')
        print('Bear runs away')

elif door == '2':
    print('You stare into the infinte abyss at Cthulhu\'s retina.')
    print('1. Blueberries.')
    print('2. Yellow jacket clothespins.')
    print('3. Understanding revolvers yelling melodies.')

    insanity = input('> ')

    if insanity == '1' or insanity == '2':
        print('Your body survives powered by a mind of jelly.')
        print('Nice work!')
    else: 
        print('The insanity rots your eyes into a pool of muck.')
        print('Nice work!')

else:
    print('You stumble around and fall on a spoon and die.')

