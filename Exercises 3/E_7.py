n = int(input())
p = int(input())
nt = n

def Ns(n):
    nS = print(f"Atenção faltam {n} segundos...")
   
   
def tempoBomba(n,p):
    if 6 <= n <= 100 and 0 <= p <= 100:
        Ns(n)
    elif n == 5 and 0 <= p <= 100:
        print("Seu tempo está acabando!")
    elif 2 <= n <= 4:
        Ns(n)
    elif n == 1 and p >= nt :
        print("Bomba desativada automaticamente!")
        return
    elif n == 1:
        print("Seja rápido. Falta 1 segundo")
    elif n == 0:
        print("Cabum!!!! Explodiu")
        return
    tempoBomba(n-1,p)
    
tempoBomba(n,p)