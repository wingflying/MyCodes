"""
BMI计算器
version: 1.0
Author:李向荣
"""

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("输入错误！请输入有效的数字。")

height = get_valid_number('身高（cm）：')
weight = get_valid_number('体重（Kg):')

bmi = weight /(height / 100) ** 2

print(f'{bmi = :.1f}')

if 18.5<= bmi <24:
  print('你的身材很棒！\n')
