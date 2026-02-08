"""
输入两个正整数计算最大公约数和最小公倍数
"""

def get_valid_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                print("请输入一个正整数！")
                continue
            return num
        except ValueError:
            print("输入错误！请输入有效的整数。")

# 输入两个正整数
print('请输入两个正整数')
x = get_valid_positive_integer('x = ')
y = get_valid_positive_integer('y = ')

# 比较x和y的大小，如果x>y就交换数值
if x > y:
    x, y = y, x
# 通过递减循环寻找最大公约数
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, (x * y // factor)))
        break
