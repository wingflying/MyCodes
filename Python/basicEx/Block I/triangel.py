"""
输入三角形的三个边长，判断是否能构成一个三角形，如果能输出计算面积
"""

print('请输入三角形的三个边长：\n')

a = float(input('请输入第一个边长:'))
b = float(input('请输入第二个边长:'))
c = float(input('请输入第三个边长:'))

if (a + b > c) and (b + c > a) and (a + c > b):
    p = (a + b + c) / 2
    print('周长： %f' % (2*p))
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：%f' % area)
else:
    print('三边长度不能构成三角形')
