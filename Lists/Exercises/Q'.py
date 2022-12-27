n = int(input())

def reverte_lista(n):
    i=0
    L = []
    while i < n:
        nome = input()
        L.append(nome)
        i += 1
    L.sort()
    for nome1 in reversed(L):
        print (nome1)
        
reverte_lista(n)