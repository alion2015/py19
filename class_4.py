"""
dir 传入 标识符 / 数据，可以查看对象内的 所有属性及方法

__方法名__ 格式的方法是 Python 提供的 内置方法 / 属性

class 类名(基类): self   类() 对象.XX()

对象.属性名=XXX 可以直接给对象设置属性，但不推荐{时机不合适会报错}，建议在类内部self.属性
self 就是对象本身的引用
在 类的外部，通过 变量名. 访问对象的 属性和方法 === 在 类封装的方法中，通过 self. 访问对象的 属性和方法

2__init__ 初始化，用来定义属性的方法
-1__del__  对象被从内存中销毁前，会被 自动 调用
1__new__ 是一个 由 object 基类提供的 内置的静态方法，主要作用有两个：在内存中为对象 分配空间；返回 对象的引用  {实现单例}
__str__  print 函数输出使用，类似tostring描述信息
__iter__ 有该方法的可以对象可以迭代(函数中返回一个实现了__next__方法的对象,将self作为参数传入；也可以是自己本身)

 __doc__ 类信息描述属性
__mro__  在多继承时判断 方法、属性 的调用 路径{method resolution order}
Python 中每一个模块都有一个内置属性 __file__ 可以 查看模块 的 完整路径
__module__ 表示当前操作的对象在那个模块
__class__ 表示当前操作的对象的类是什么
__dict__ 属性输出类或对象中的所有属性

属性初始值，可以设置为 None，可以将 None 赋值给任何一个变量，表示什么都没有{定义空变量} XX is None

is 用于判断 两个变量 引用对象是否为同一个 == 用于判断 引用变量的值 是否相等

属性名或者方法名前 增加 两个下划线，定义的就是 私有 属性或方法

添加_类名 可以访问私有属性和方法，但不推荐

类属性：定义类似java中普通属性，作用相当于static属性
如果使用 对象.类属性 = 值 赋值语句，只会 给对象添加一个属性，而不会影响到 类属性的值

@classmethod类方法：可以直接访问 类属性 或者调用其他的 类方法
通过 类名. 调用 类方法，调用方法时，不需要传递 cls 参数{cls类本身的引用}

@staticmethod静态方法：不需要访问实例属性也不需要访问类属性的方法
 类名. 调用 静态方法

super().XX()调用父类中方法实现

包 是一个 包含多个模块 的 特殊目录
目录下有一个 特殊的文件 __init__.py
使用 import 包名 可以一次性导入 包 中 所有的模块
要在外界使用 包 中的模块，需要在 __init__.py 中指定 对外界提供的模块列表
    # 从 当前目录 导入 模块列表
    from . import send_message
    from . import receive_message

property属性：可以有内部计算的属性
    1）@property 装饰器xx.setter/deleter
    2） BAR = property(get_bar, set_bar, del_bar, "description...")

元类：type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
    属性中可以传入方法
    元类就是类的类
    元类的主要目的就是为了当创建类时能够自动地改变类。


"""


class Cat:
    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name
        Cat.count += 1

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def __secret(self):
        pass

    @classmethod
    def get_count(cls):
        print(cls.count)

    @staticmethod
    def run():
        pass


class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作,防止单例中多次初始化
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:       # if not
            print("初始化音乐播放器")
            MusicPlayer.init_flag = True


if __name__ == '__main__':
    tom = Cat("Tom")
    if tom is not None:
        tom.eat()
        tom._Cat__secret()  # 添加_类名 可以访问私有属性和方法，但不推荐

