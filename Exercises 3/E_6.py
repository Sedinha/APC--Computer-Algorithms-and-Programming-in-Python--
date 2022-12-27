#----------------------------# Média Salarial # ----------------------------------------#
N=int(input())
din0=0
i=0
    
while i < N:
    func = input().split(",")
    s = float(func[1])
    din0 += s
    if i == N:
        din0 = din0 - s
        if N == 1:
            result = din0/(i)
            print(f"{result:.2f}")
            break
    i += 1
if N == 0:
    print("Não tem média")
if N != 0:
    result = din0/(i)
    print(f"{result:.2f}")
        

#----------------------------# Maior Salario # ----------------------------------------#
din=0
din2=0
nome2= ""
i=0
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
    din = n1 - din
    if din > 0 :
        din = n1
        nome2 = nome
    else:
        din = n1+(din*-1)
    i += 1
#----------------------------# Menor Salario # ---------------------------------------------#
nome3 = ""
i=1
n2=0

while i <= N:
    func = input().split(",")
    if N == 0:
        print("Não tem")
        break
    if i == N:
        print(f"{nome3} {din:.2f}")
        break
    n2 = float(func[1])
    nome =  func[0]
    din2 = n2 - din2
    if din2 > 0 and i == 0:
        din2 = n2
        nome3 = nome
    if din2 > 0 :
        if i == 0:
            False
        else:
            din2 = n2+((din2)*-1)
    else:
        din2 = n2
        nome3 = nome

    i += 1