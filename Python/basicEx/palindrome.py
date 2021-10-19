"""
判断是否回文数
"""


def is_palindrome(num):
    """判断一个数是否回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_prime(num):
    """判断一个数是否素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if (num != 1) else False


def main():
    num = int(input('请输入正整数：'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)


if __name__ == '__main__':
    main()
