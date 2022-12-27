n = int(input())

def n_alunos(n):
    d = {}
    i = 0
    while i < n:
        nome, nota = input().split(", ")
        nota = float(nota)
        d[nome] = nota
        i += 1
    return d

# Inicio do programa #

d = n_alunos(n)
lista_nomes = []
sua_nota = float(input())
i = 0
for nome,nota in d.items():
    if nota == sua_nota:
        lista_nomes.append(nome)
if len(lista_nomes) == 0:
    print("Você foi o único aluno com essa nota.")
else:
    lista_nomes = sorted(lista_nomes)
    for nome in lista_nomes:
        if nome != lista_nomes[-1]:
            print(f'{nome}',end='/')
        else:
            print(f'{nome}')