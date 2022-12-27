A,B,C = map(int,input().split())

def areas(A,B,C):
    r = int((A*B))
    t = int(((B*C)/2))
    tp = int((((B+C)*A)/2))
    print(r)
    print(t)
    print(tp)

areas(A,B,C)