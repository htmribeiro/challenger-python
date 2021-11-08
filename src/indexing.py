import collections
import re
import os

w_index = 1
d_word_base = dict()
d_index_word = dict()

def get_word_index(word):
  i = 0
  if word in d_word_base.keys():
    i = d_word_base[word]['index']
  return i


def dict_build(fname="", wl=[]):
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

    flist = d_index_word[ get_word_index(word) ]['files']
    if fname not in flist:
      flist.append(fname)
      flist.sort()

if __name__ == '__main__':
  path = "C:\\Users\\p22.ribeiro\\OneDrive\\repocode\\challenge-python\\dataset"
  os.chdir(path)
  
  def read_text_file(file_path, filename):
    with open(file_path, 'r') as arquivo:
      frase = arquivo.read()

    for remove in '!@#$%&*()<>:;,./?\|][}{=+-`^"~£_':
      frase = frase.replace(remove, ' ').lower()
      
    remove = re.compile(r"[^\w][0-9]+")
    lista_palavra = frase.lower().split()
    w1 = list(set([re.sub(remove, "", word) for word in lista_palavra]))

    dict_build(filename, w1)
  
  for file in os.listdir():
    if file.endswith(""):
      file_path = f"{path}\{file}"
      filename = file_path.rsplit("\\",1)[-1]
      read_text_file(file_path, filename)

  od = collections.OrderedDict(sorted(d_word_base.items()))
  for k, v in od.items():
    print('word: {:<20} index: {:<10} -- files: {}'.format(k,
          v['index'], v['files']))
  print('-'*50)
  for k, v in d_index_word.items():
    print('index: {:<10} word: {:<20} -- files: {}'.format(k,
          v['word'], v['files']))

print("{:*^50}".format(' End Dataset '))
