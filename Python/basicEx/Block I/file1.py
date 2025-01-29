"""
文件操作
"""
# import time


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')

    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as f:
            i = 0
            for line in f:
                i += 1
            print(i)

    f.close()


if __name__ == '__main__':
    main()
