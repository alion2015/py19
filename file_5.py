"""
open->read/write->close
open参数 r/w/a 文件头开始读，文件尾追加；读的文件不存在就报错，其余会新建；w会覆盖原有文件；
readline 方法可以一次读取一行内容
"""
import os


def read_big_file(name):
    # 打开文件
    file = open(name)
    while True:
        # 读取一行内容
        text = file.readline()
        # 判断是否读到内容
        if not text:
            break
        # 每读取一行的末尾已经有了一个 `\n`
        print(text, end="")
    # 关闭文件
    file.close()


def test_os():
    path = os.getcwd()
    os.path.isdir(path)
    os.listdir(path)
    os.mkdir("test")
    os.chdir("test")
    os.rmdir("test")


if __name__ == '__main__':
    test_os()
