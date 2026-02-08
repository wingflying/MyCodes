"""
将华氏温度转换为摄氏温度
作者：李向荣
"""

while True:
    try:
        f = float(input('请输入华氏温度：'))
        c = (f - 32) / 1.8
        print('%.1f华氏度  = %.1f摄氏度 ' % (f, c))
        break
    except ValueError:
        print("输入错误！请输入有效的数字温度值。")
        continue
