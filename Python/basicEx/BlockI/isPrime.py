"""
输入一个整数，判断是否是素数
"""

from math import sqrt

while True:
    try:
        num = int(input('请输入一个正整数：'))
        if num <= 0:
            print("请输入一个正整数！")
            # continue75
        break
    except ValueError:
        print("输入错误！请输入有效的整数。")

end = int(sqrt(num))

is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
