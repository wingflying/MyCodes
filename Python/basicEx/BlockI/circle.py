"""
输入半径计算圆的周长和面积
"""

import math

while True:
    try:
        radius = float(input('请输入圆的半径：'))
        perimeter = 2 * math.pi * radius
        area = math.pi * radius * radius
        print('周长：%.2f' % perimeter)
        print('面积：%.2f' % area)
        break
    except ValueError:
        print("输入错误！请输入有效的数字半径值。")
        continue
