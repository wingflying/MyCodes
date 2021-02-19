"""
功能：输入M和N计算C(M, N)
"""

m = int(input('m = '))
n = int(input('n = '))

fm = 1
for num in range(1, m + 1):
    fm = fm * num

fn  = 1
for num in range(1, n + 1):
    fn = fn * num

fmn = 1
for num in range(1, m - n + 1):
    fmn = fmn * num

print(fm // fn // fmn)