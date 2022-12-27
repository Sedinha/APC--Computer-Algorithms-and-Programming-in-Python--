din=0
i=0
while True:
    func = input().split(",")
    s = float(func[1])
    din += s
    i += 1
    if func[0] == "Fim":
        din = din - s
        if i == 1:
            result = din/(i)
            print(f"{result:.2f}")
            break
        else:
            result = din/(i-1)
            print(f"{result:.2f}")
            break
