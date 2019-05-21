""" 基础
注释
格式化输出 % (price, "25")
输入
/ ；//；% ；** 除；除后取整；取余；幂
elif or ：
函数5件套
pass 占位

当 函数/方法 执行 出现异常，会 将异常传递 给 函数/方法 的 调用一方,如果 传递到主程序，仍然 没有异常处理，程序才会被终止
在开发中，可以在主函数中增加 异常捕获

import a,b 或则分行；import 模块名1 as 模块别名；from 模块名1 import 工具名{导入优先当前路径，然后才是系统路径}
在导入文件时，文件中 所有没有任何缩进的代码 都会被执行一遍！！

eval() —> 将字符串 当成 有效的表达式 来求值 并 返回计算结果

false : NONE;False(布尔类型)；所有的值为零的数；为空的高阶变量

正则表达式import re# 使用match方法进行匹配操作 result = re.match(正则表达式,要匹配的字符串)# 使用group方法来提取数据result.group()

with 语法用于简化资源操作的后续清除操作，是 try/finally 的替代方法，实现原理建立在上下文管理器之上。此外，Python 还提供了一个 contextmanager 装饰器，更进一步简化上下管理器的实现方式。

装饰器：@w1 执行w1函数 ，并将 @w1 下面的函数作为w1函数的参数，即：@w1 等价于 w1(f1)
"""
import random


def _learn():
    """
    def my_name(X) : return 函数5件套
    """
    price = float(input("单价："))  # 输入中读取单价float格式
    print("价格是：%d,年龄是：%s" % (price, "25"),end="")  # 格式化输出，使用""替换原来的换行,%x 可以以 16 进制 输出数字
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


def demo_exception():
    num = int(input("请输入整数："))
    result1 = 8 / num
    print(result1)

    # 抛出异常
    raise Exception("密码长度不够")


def test():
    pass  # 占位符，保证结构完整


if __name__ == '__main__':
    """ 用于添加测试代码。防止被import时被执行
     __name__ 是 Python 的一个内置属性，记录着一个 字符串；
     如果 是被其他文件导入的，__name__ 就是 模块名；
     如果 是当前执行的程序 __name__ 是 __main__
    """
    test()  # 函数名()才会执行
    try:
        demo_exception()
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as result:
        print("未知错误 %s" % result)
    else:
        print("没有异常才会执行的代码")
    finally:
        print("无论是否有异常，都会执行的代码")
