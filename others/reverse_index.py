def main():
    for cont in range(0, 44):
        with open("C:\\Users\\p22.ribeiro\\OneDrive\\repocode\\challenge-python\\dataset\\{}".format(cont), "r", encoding="cp1252") as arquivo:
            frase = arquivo.read()

    for remove in '!@#$%&*()<>:;,./?\|][}{=+-"~£':
        frase = frase.replace(remove, ' ').lower()

    lista_frase = frase.split()
    clear_list = set(lista_frase)
    clear_list = sorted(clear_list)
    comprimento = len(clear_list)

    # print(lista_frase)
    # print(comprimento)

    indice = 0
    dicionario_palavra = dict()
    while indice < comprimento:
        for palavra in clear_list:
            dicionario_palavra = [indice, palavra]

            print(dicionario_palavra) # Tirar este print
            indice += 1
main()


