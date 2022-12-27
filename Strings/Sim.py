din=0
nome2 = ""
i=0
n2=0
while True:
    func = input().split(",")
    if func[0] == "Fim":
        func[1] = 0
        if i == 0:
            print("Não tem")
            break
        print(f"{nome2}")
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