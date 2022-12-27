a = int(input())
b = int(input())
c = int(input())
p1 = input()
p2 = input()

if a >= 0 and b >= 0 and c >= 0:
    pA = (p1*(a+b))
    pB = (p2*(b+c))
    pC = pA + pB
    pD = (pC*(a+c))
print(pD)
