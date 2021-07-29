import sys
import time
# TODO login
x = 'passcode'
passcode_counter = 0
print('Enter Username:')
name = input('')
print('Password:')
y = input('')
if x == y:
    print('Hello, welcome {0}!'.format(name))
    run = False
elif x != y:
    print('Huh sorry this isn\'t {0}'.format(name))
    run = True
# does not stop loop until correct
while run:
    passcode_counter +=1
    print('Password:')
    y = input('')
    print('Tries: {0}'.format(passcode_counter))
    if x == y:
        print('Hello, welcome {0}!'.format(name))
        run = False
    elif passcode_counter == 3:
        print('{0} Account is locked! For 15 seconds'.format(name))
        time.sleep(15)
        run = True
    elif passcode_counter == 7:
        print('Your Finshed!!!')
        sys.exit()
    elif passcode_counter > 8:
        print('You Hacked me?')


for i in [0, 1, 2]:
    print('Marcus Mellv')

for i in range(3):
    print('is Here!')


#