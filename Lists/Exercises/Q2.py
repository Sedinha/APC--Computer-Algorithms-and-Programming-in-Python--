n = int(input())

def players(n):
    P = []
    I = []
    for p in range(n):
        p = input()
        P.append(p)
    impostores = input().split()
    I.extend(impostores)
    i=0
    for a in I:
        while True:
            if a in P:
                P.remove(a)
            else:
                break  
    print(*P)
    
players(n)