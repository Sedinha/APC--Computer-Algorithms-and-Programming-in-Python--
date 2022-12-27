def paron(L):
    contador = 0
    vogais = ["a","e","i","o","u","A","E","I","O","U"]
    novoL = []
    contador = 0
    i = 0
    while i < len(L):
        for v in vogais:
            contador += L[i].count(v)
        if contador % 2 == 0:
            novoL.append(L[i])
        i += 1
        contador = 0
    return novoL

print(paron())



                
            
    