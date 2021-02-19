"""
输入两个正整数计算最大公约数和最小公倍数
"""
## 输入两个正整数
print('请输入两个正整数')
x = int(input('x = '))
y = int(input('y = '))

## 比较x和y的大小，如果x>y就交换数值
if x > y:
    x, y = y, x
##通过递减循环寻找最大公约数
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' %  (x, y, (x * y // factor)))
        break
