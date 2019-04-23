""" 基础
注释
格式化输出 % (price, "25")
输入
/ ；//；% ；** 除；除后取整；取余；幂
乘法拼接字符串
elif or ：
函数5件套
"""
import random


def _learn():
    """
    def my_name(X) : return 函数5件套
    """
    price = float(input("单价："))  # 输入中读取单价float格式
    print("价格是：%d,年龄是：%s" % (price, "25"),end="")  # 格式化输出，使用""替换原来的换行
    print("*" * 100)  # 乘法可以拼接字符串

    # 条件判断
    if price < 0 or (price < 10 and price < 20):
        print("1")
    elif price < 30:
        print("2")
    else:
        print("3")

    # 随机数
    a = random.randint(2, 5)
    print(a)

    # 循环
    n = 3
    while n > 0:
        print(n)
        n -= 1


def test():
    n = 6


if __name__ == '__main__':
    test()  # 函数名()才会执行
