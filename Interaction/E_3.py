din=0
i=0
n2=0
while True:
    func = input().split(",")
    if func[0] == "Fim":
        func[1] = 0
    n1 = float(func[1])
    n2 = n1
    din = n1 - din
    if din > 0 :
        din = n1
    else:
        din = n1+(din*-1)
    if func[0] == "Fim":
        if func[0] == "Fim" and din > 0:
            din = n1 + din            
        if i == 0:
            print("Não tem")
            break
        print(f"{din:.2f}")
        break
    i += 1