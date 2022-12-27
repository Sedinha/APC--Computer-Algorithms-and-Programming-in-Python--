def busca_string(frase,string):
    cont = 0
    i = -1
    while True:
        i = frase.find(string, i+1)
        if i == -1:
            return cont
        else:
            cont += 1
        
frase = input("digite frase: ")
palavra = input("Digite palavra :")
print(f"Possui {busca_string(frase,palavra)} ocorrencias de string '{palavra}'.")
