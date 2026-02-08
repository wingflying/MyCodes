"""
分段函数求职
"""

x = float (input ('Please input the number:\n'))

if (x > 1):
    y = 3 * x - 5
elif (x >= -1):
    y = x + 2
else:
    y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))


