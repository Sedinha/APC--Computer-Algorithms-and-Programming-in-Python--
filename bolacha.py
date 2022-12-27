m = int(input())
n = int(input())
k = int(input())

def pacotesDeBolachas(m,n,k):
    if n >= 1 and m >= n and k >= 1:
        result = (m//n)
        # k = numero de bolachas
        result2 = k*n
        print(result2)

pacotesDeBolachas(m,n,k) 
