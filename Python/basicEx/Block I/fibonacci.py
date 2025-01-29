"""
Fibonacci sequence producton
"""
x = 1
y = 1

num = int(input('请输入计算数列长度：'))

for i in range(1, num+1):
    x, y = y, x + y
    print(x, end = ' ')
    if i % 10 == 0:
        print('\n');


