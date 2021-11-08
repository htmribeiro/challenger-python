import os
import re

path = "C:\\Users\\p22.ribeiro\\OneDrive\\repocode\\challenge-python\\dataset"
os.chdir(path)

# for filename in dirs:
#     if filename.endswith(""):
#         print(os.path.join(path, filename))

def read_text_file(file_path):
  with open(file_path, 'r') as arquivo:
    frase = arquivo.read()

  remove = re.compile(r"[^\w]+")

  lista_palavra = frase.lower().split()
  w1 = list(set([re.sub(remove, "", word) for word in lista_palavra]))
  print(w1)

for file in os.listdir()[0]:
  if file.endswith(""):
    file_path = f"{path}\{file}"
    # file_path = f"{path}\{0}"
    print()
    filename = file_path.rsplit("\\",1)[-1]
    print(filename)
    print()      
    read_text_file(file_path)
    
