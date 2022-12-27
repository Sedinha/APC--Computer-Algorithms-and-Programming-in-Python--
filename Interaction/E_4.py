#----------------------------# Média Salarial # ----------------------------------------#
N=int(input())
din=0
i=0
while i < N:
    func = input().split(",")
    s = float(func[1])
    din += s
    if i == N:
        din = din - s
        if N == 1:
            result = din/(i)
            print(f"{result:.2f}")
            break
    i += 1
if N == 0:
    print("Não tem média")
if N != 0:
    result = din/(i)
    print(f"{result:.2f}")
        

#----------------------------# Maior Salario # ----------------------------------------#
din=0
nome2= ""
i=0
n2=0
while i < N:
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
        nome = nome2
    else:
        din = n1+(din*-1)          
    if i == 0:
        print("Não tem")
        break
    if i == N:
        print(f"{din:.2f}")
        break
    i += 1
#------------------------# Menor Salario # ---------------------------------------------#
din=0
nome2 = ""
i=0
n2=0

while i < N:
    func = input().split(",")
    if N == 0:
        print("Não tem")
        break
    if i == N:
        print(f"{nome2} {din:.2f}")
        break
    n1 = float(func[1])
    nome =  func[0]
    n2 = n1
    din = n1 - din
    if din > 0 and i == 0:
        din = n1
        nome2 = nome
    if din > 0 :
        if i == 0:
            False
        else:
            din = n1+(din*-1)
    else:
        din = n1
        nome2 = nome

    i += 1
