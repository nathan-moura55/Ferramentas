from os import chdir, listdir
from os.path import isfile

cam = input('Digite o caminho: ')

chdir(cam)

soma = 0
for c in listdir():
    if isfile(c):
        print(cam + '\\' + c)
        soma += 1
print()
print(f'{soma} arquivos encontrados.')