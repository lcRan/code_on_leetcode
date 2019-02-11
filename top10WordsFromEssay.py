

# 有一个纯英文的文本， 给定文件的路径， 将文本中出现 top 10 的单词打印出来
def get_words(fpath):
    a_list = ('a', 'b', 'c', 'd', 'e', 'f', 'g',
              'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', ' ', '-',
              )
    result = ''
    file = open(fpath, 'r').read()
    for w in file.lower():
        if w in a_list:
            result += w
    words = result.split()
    return words


def words_count(words):
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


def sort_words(dic):
    l = []
    for w in dic:
        tuple_dict = (dic[w], w)
        l.append(tuple_dict)
    sorted_list = sorted(l, key=lambda x: x[0], reverse=True)
    # print(sorted_list)
    return sorted_list


if __name__ == '__main__':
    fpath = 'server.txt'
    words = get_words(fpath)
    words_dic = words_count(words)
    sorted_list = sort_words(words_dic)
    for i in range(10):
        print(sorted_list[i])
        print()