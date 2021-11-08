import collections

w_index = 1
d_word_base = dict()
d_index_word = dict()


def get_word_index(word):
    i = 0
    if word in d_word_base.keys():
        i = d_word_base[word]['index']
    return i


def dict_build(fname="0.txt", wl=[]):
    global w_index
    for word in wl:
        if word not in d_word_base.keys():
            v = dict()
            v['index'] = w_index
            v['files'] = []
            d_word_base[word] = v

            x = dict()
            x['word'] = word
            x['files'] = []
            d_index_word[w_index] = x
            w_index += 1

        flist = d_word_base[word]['files']
        if fname not in flist:
            flist.append(fname)
            flist.sort()

        flist = d_index_word[get_word_index(word)]['files']
        if fname not in flist:
            flist.append(fname)
            flist.sort()


if __name__ == '__main__':

    with open("C:\\Users\\acavi\\Downloads\\desafioPython\\0.txt", "r", encoding="cp1252") as arquivo:
        w1 = arquivo.read()
        w1 = set(w1)
        w1 = sorted(w1)

    with open("C:\\Users\\acavi\\Downloads\\desafioPython\\1.txt", "r", encoding="cp1252") as arquivo:
        w2 = arquivo.read()

    with open("C:\\Users\\acavi\\Downloads\\desafioPython\\2.txt", "r", encoding="cp1252") as arquivo:
        w3 = arquivo.read()

    with open("C:\\Users\\acavi\\Downloads\\desafioPython\\3.txt", "r", encoding="cp1252") as arquivo:
        w3 = arquivo.read()

    """w1 = ['madeira', 'Queijo', 'Hamilton', 'melancia', 'mexirica']
    w2 = ['arvore', 'Hamilton', 'laranja', 'banana', 'caja']
    w3 = ['madeira', 'Hamilton', 'melancia', 'mexirica']"""

    dict_build('f1', w1)
    dict_build('f2', w2)
    dict_build('f3', w3)
    dict_build('f4', w2)

    od = collections.OrderedDict(sorted(d_word_base.items()))
    for k, v in od.items():
        print('word: {:-<30} -- index: {:->5} -- files: {}'.format(k, v['index'], v['files']))
    print('-' * 50)
    for k, v in d_index_word.items():
        print('index: {:-<30} word: {:->5} files: {:-}'.format(k, v['index'], v['files']))
