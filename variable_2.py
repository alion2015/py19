"""
列表
元组
字典
字符串
公共方法

tuple(列表)/list(元组) 转换
1.tuple()->list[]->dict{:,:}->set{}
(元组)->[列表]->{:,:字典}->{set}
len/del/max/min公共函数
可用运算符+ /* /in/not in /(> < ==等比较)
2.for x in range(6):else(无break完成循环是才执行)
    循环体代码
else:
    没有通过 break 退出循环，循环结束后，会执行的代码
3.slice 切片[开始索引:结束索引:步长]   ---有头无尾;一个：步长1;无：首尾同，指定元素
4.dict.items()/keys()/values()
5.列表生成式 [x *x for x in range(1,11) if x %2==0][终式 for筛选]
[x*x if x>30 else -x*x for x in range(100)]终式有if必有else筛选只能有if

just strip extend update

which python3
#! /usr/bin/python3(shebang写在文件首行指明 执行这个脚本文件 的 解释程序)

r"..." 不转义：:所见即所得，不被str转义

全局变量名前应该增加 g_ 或者 gl_ 的前，默认不可修改，可通过 global XXX 申明后再修改(nonlocal XXX 闭包外的数据声明到本地)

列表变量调用 += 本质上是在执行列表变量的 extend 方法，不会修改变量的引用{没有赋值过程}

6.a, b = b, a  python中交换两个变量的值

id(item) 输出item引用对象的地址

isinstance('abc', Iterable) 判断是否可迭代对象
可以通过iter()函数获取这些可迭代对象的迭代器。然后我们可以对获取到的迭代器不断使用next()函数来获取下一条数据

copy.copy/deepcopy浅拷贝与深拷贝

str = "nihao{}shenm,e{}hah{}".format(342,2,"yeh")字符串格式化的一种方式

str = "nihao" if 4 > 5 else "buhao"
"""

import base_1 as dl  # 引入模块


def _list():
    """
    append/insert/extend 添加
    del/remove/pop 删除   {del是关键字}
    len、count统计     {len是函数}
    sort、reverse 排序和反转
    for name in list：遍历
    index->索引->读写指定值
    """
    name_list = ["zhangsan", "lisi", "wangwu"]
# 1. 取值和取索引
    # list index out of range - 列表索引超出范围
    print(name_list[2])

    # 知道数据的内容，想确定数据在列表中的位置
    # 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
    print(name_list.index("wangwu"))

# 2. 修改
    name_list[1] = "李四"
    # list assignment index out of range
    # 列表指定的索引超出范围，程序会报错！
    # name_list[3] = "王小二"

# 3. 增加
    # append 方法可以向列表的末尾追加数据
    name_list.append("王小二")
    # insert 方法可以在列表的指定索引位置插入数据
    name_list.insert(1, "小美眉")

    # extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
    temp_list = ["孙悟空", "猪二哥", "沙师弟"]
    name_list.extend(temp_list)

# 5. 统计
    # len(length 长度) 函数可以统计列表中元素的总数
    list_len = len(name_list)
    print("列表中包含 %d 个元素" % list_len)

    # count 方法可以统计列表中某一个数据出现的次数
    count = name_list.count("张三")
    print("张三出现了 %d 次" % count)
# 6.排序
    # 升序
    name_list.sort()
    # 降序
    name_list.sort(reverse=True)
    # 逆序（反转）
    name_list.reverse()
# 7.迭代遍历
    for my_name in name_list:
        print("我的名字叫　%s" % my_name)
# 4. 删除
    # remove 方法可以从列表中删除指定的数据,第一个匹配值
    name_list.remove("wangwu")
    # pop 方法默认可以把列表中最后一个元素删除
    name_list.pop()
    # pop 方法可以指定要删除元素的索引
    name_list.pop(3)

    # (知道)使用 del 关键字(delete)删除列表元素
    # del 关键字本质上是用来将一个变量从内存中删除的
    # 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
    del name_list[1]

    # clear 方法可以清空列表
    name_list.clear()


def _tuple():
    """
    []->()，只读，通常保存的数据类型是不同的
    只有index和count操作
    """
    # 只包含一个元素时，需要在元素后面添加逗号
    info_tuple = (50,)


def _dict():
    """
    指定k->读写(可以是新增)
    pop(k),len(name),update(合并)     p长更
    """
    xiaoming_dict = {"name": "小明"}

# 1. 取值
    print(xiaoming_dict["name"])
    # 在取值的时候，如果指定的key不存在，程序会报错！
    # print(xiaoming_dict["name123"])

# 2. 增加/修改
    # 如果key不存在，会新增键值对
    xiaoming_dict["age"] = 18
    # 如果key存在，会修改已经存在的键值对
    xiaoming_dict["name"] = "小小明"

# 3. 删除
    xiaoming_dict.pop("name")
    # 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
    # xiaoming_dict.pop("name123")
# 4. 统计键值对数量
    print(len(xiaoming_dict))

# 5. 合并字典
    temp_dict = {"height": 1.75,
                 "age": 20}

    # 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
    xiaoming_dict.update(temp_dict)

# 6. 清空字典
    xiaoming_dict.clear()
# 7. 迭代遍历字典
    # 变量k是每一次循环中，获取到的键值对的key
    for k in xiaoming_dict:
        print("%s - %s" % (k, xiaoming_dict[k]))


def _str():
    """
    len,count,index  长个位置
    is,find,replace 找查体
    ljust、center 对齐
    strip，lstrip 去空白
    split、join 分(默认空白字符)合
    """
    hello_str = "hello hello"

# 1. 统计字符串长度
    print(len(hello_str))
# 2. 统计某一个小（子）字符串出现的次数
    print(hello_str.count("llo"))
# 3. 某一个子字符串出现的位置,不存在会报错
    print(hello_str.index("llo"))
# 4. 切片 字符串[开始索引:结束索引:步长]---左包含
    print(hello_str[::-1])


if __name__ == '__main__':
    # dl.test()
    # _list()
    # _tuple()
    # _dict()
    _str()
