"""
输入年份，如果是闰年输出True，否则输出False
"""

year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap)

if(is_leap):
    print('% is leap year' % year)
else:
    print('%i is not leap year' % year)
