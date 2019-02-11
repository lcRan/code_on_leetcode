import os


# 编写一个程序，能在当前目录以及当前目录的所有子目录下
# 查找文件名包含指定字符串的文件，并打印出相对路径。
# os.path.abspath(path)，显示path在操作系统中的绝对路径
# os.path.join(path, x)，将path和x拼接成当前操作系统兼容的路径形式
# os.listdir(path)，输出当前目录下的文件及子目录为list类型
# os.path.isdir(path) and os.path.isfile(path)判断路径为目录还是文件，注意参数为path，
# 之前在这里出现了很多错误，直接输文件名的话，没有该文件就直接显示False

def find_cur(string, path):
    l = []

    for x in os.listdir(path):
        if os.path.isfile(path+'/'+x):
            if string in x:
                l.append(os.path.abspath(x))

    if not l:
        print('no {} in {}'.format(string, os.path.abspath(path)))

    else:
        print(l)


def deeper_dir(string='', p='..'):
    find_cur(string, p)
    for x in os.listdir(p):
        pp = p
        if os.path.isdir(pp):
            pp = os.path.join(pp, x)
            if os.path.isdir(pp):
                deeper_dir(string, pp)


if __name__ == '__main__':
    deeper_dir('txt')
