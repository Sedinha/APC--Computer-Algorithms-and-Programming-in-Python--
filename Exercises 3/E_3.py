n1,n2,n3 = map(int,input().split())
r = input()
v = n1,n2,n3
t = len(v)

if r == "A":
    print("Aritmetica")
    r1 = (n1+n2+n3)/t
    print(f"{r1:.2f}")
    
elif r == "P":
    print("Ponderada")
    p1,p2,p3 = map(int,input().split())
    r2 = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
    print(f"{r2:.2f}")

elif r == "H":
    print("Harmonica")
    r3 = (t)/((1/n1)+(1/n2)+(1/n3))
    print(f"{r3:.2f}")
    
else:
    print("Operacao inexistente")