# """
# 按类的机制来描述数字时钟
# """

from time import sleep, time, localtime


class Clock(object):
    """数字时钟"""
    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法"""
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_second)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 23:
                    self._hour = 0

    def show(self):
        """显示世界"""
        return ('%02d:%02d:%02d' % (self._hour, self._minute, self._second))


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
