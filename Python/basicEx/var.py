"""
使用变量与字面变量
"""

# i = 5
# print(i)
# i = i + 1
# print(i)
#
# s = '''This is a multi-line string.
# This is the second line. '''
# print(s)
#
# print('Value is', i)
# print('I repeat, the value is', i)

number = 23
running = True

while running:
    guess = int(input('Enter an integer:'))

    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('NO, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')

print('Done!')
