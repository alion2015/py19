"""
函数的 实参/返回值 都是是靠 引用 来传递来的

可变类型的数据变化，是通过 方法 来实现的，赋值了一个新的数据，引用会修改
可变是指可改变内容但不改变引用地址，目前字典和列表可以。
在函数内部，针对参数使用 赋值语句，不会影响调用函数时传递的 实参变量 ：{赋值修改引用，对元数据无修改}
可变类型，在函数内部，使用 方法 修改了数据的内容，同样会影响到外部的数据

可利用元组作为函数返回值，同时返回多个参数，也可用多个参数接收

定义函数时，可以给 某个参数 指定一个默认值，具有默认值的参数就叫做 缺省参数
     带有默认值的缺省参数 在参数列表末尾
     有 多个缺省参数，需要指定参数名
         def print_info(name, title="", gender=True):
         print_info("老王", title="班长")

需要 一个函数 能够处理的参数 个数 是不确定的，这个时候，就可以使用 多值参数{两种实现方式}
    参数名前增加 一个 * 可以接收 元组        *args —— 存放 元组 参数，前面有一个 *
    参数名前增加 两个 * 可以接收 字典        **kwargs —— 存放 字典 参数，前面有两个 *

递归出口：参数满足一个条件 时，函数不再执行
"""


def measure():
    """返回当前的温度"""

    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")
    # return (temp, wetness)如果一个函数返回的是元组，括号可以省略
    return temp, wetness


def demo(num, *args, **kwargs):  # 贪婪的参数识别
    print(num)
    print(args)
    print(kwargs)


if __name__ == '__main__':
    result = temp1, wetness1 = measure()
    demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
    arg = (1, 2, 3, 4, 5)
    kwarg = {"name": "小明", "age": 18, "gender": True}
    demo(1, arg, kwarg)     # 贪婪的元组中存放不同类型元素，可以是字典，需要拆包  //错误
    demo(1, arg=arg, kwarg=kwarg)     # 拆包                                      //错误
    demo(1, *arg, **kwarg)     # 拆包
    pass
