"""
控制流
"""
while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    # if len(s) < 3:
    #     print('Too small')
    #     continue
    # print('Input is of sufficient length')
    print('Length of the string is', len(s))
print('Done!')