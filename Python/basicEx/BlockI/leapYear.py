"""
输入年份，如果是闰年输出True，否则输出False
"""

while True:
    try:
        year = int(input('请输入年份：'))
        break
    except ValueError:
        print("输入错误！请输入有效的年份。")

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap)

if(is_leap):
    print('%d是闰年' % year)
else:
    print('%d不是闰年' % year)
