nu = int(input())
n = nu

def deivis_sequence(n):
    if 3 < n <= 31:
        while n>0:
            d = deivis_sequence(n-1)
            print(d)
    elif 2 < nu <= 3:
        a1 = ((nu-2)+(nu-1))-1
        return a1
    elif 1 <= nu <= 2:
        return nu
        
deivis_sequence(nu)