num = list(map(int,input().split()))
def conta_louca(num):
    i=0
    r = 0
    while len(num) > 1:
        num[1] = num[i]*2 + num[i+1]*0.5
        del num[0]
    
    print(f"{num[0]:.2f}")
        
conta_louca(num)
    