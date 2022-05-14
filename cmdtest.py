#cmdtest.py
import time

if __name__ == '__main__':
    framelist = []
    while True:
        for i in range(0, 140):
            if i < 20:
                print("南北路口状态：直行 绿灯, 左转 红灯, 右转 绿灯， 剩余时间 {}s; 东西路口状态：红灯; 剩余时间 {}s".format(i, 60 - i), end="\r")
            elif i < 60:
                print("南北路口状态：直行 红灯, 左转 绿灯, 右转 绿灯， 剩余时间 {}s; 东西路口状态：红灯; 剩余时间 {}s".format(i - 20, 60 - i), end="\r")
            else:
                print("南北路口状态：直行 红灯, 左转 红灯, 右转 绿灯， 剩余时间 {}s; 东西路口状态：绿灯; 剩余时间 {}s".format(140 - i, 140 - i), end="\r")

            time.sleep(1)


