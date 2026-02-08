"""
输入一个正整数判断是否素数
"""
#from math import sqrt
import math

num = int(input('请输入一个正整数：'))
count = 0

for i in range(2, num):
    is_prime = True
    for factor in range(2, int(math.sqrt(i) + 1)):
        if i % factor == 0:
            is_prime = False
            break

    if is_prime:
        print(i, end = ' ')
        count += 1
        if count % 10 == 0:
            print('\n')

print('\n共有%d个素数' % count)

# for num in range(2, 100):
#     is_prime = True
#     for factor in range(2, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')