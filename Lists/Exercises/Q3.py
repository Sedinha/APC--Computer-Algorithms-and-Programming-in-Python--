seq = map(int,input().split())
n = int(input())

def mult_n(seq,n):
    t = []
    for n0 in seq:
        if n0 % n == 0:
            t.append(n0)
    print(*t)
            
mult_n(seq,n)
    
    