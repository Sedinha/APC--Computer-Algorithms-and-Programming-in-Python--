din0 = 0
din=0
din2=0
nome2= ""
i=1
n2=0
while i+1 <= N:
    func = input().split(",")
    if N == 0:
        print("Não tem")
        break
    if i == N:
        print(f"{nome2} {din:.2f}")
        break
    n1 = float(func[1])
    nome = func[0]
    n2 = n1
    din = n1 - din
    if din > 0 :
        din = n1
        nome2 = nome
    else:
        din = n1+(din*-1)
    i += 1
