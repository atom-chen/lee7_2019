# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/6 0006 21:19'
__author__ = 'Lee7'
import time


def sing():
    """唱歌五秒钟"""
    for i in range(5):
        print("我一路向北，离开有鱼的季节")
        time.sleep(1)


def dance():
    """跳舞五秒钟"""
    for i in range(5):
        print("大家好 我是练习两年半的偶像练习生蔡徐坤\n鸡你太美")
        time.sleep(1)


def main():
    sing()
    dance()


if __name__ == "__main__":
    main()