"""
完美数是所有真因子之和相加等于自身；
通过循环计算1～10000之内所有的完美数；
"""
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)

