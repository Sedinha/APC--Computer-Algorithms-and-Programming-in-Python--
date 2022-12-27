nu = int(input())
n = nu

def deivis_sequence(n,nu):
    if nu > n-2:
        d2 = deivis_sequence(n,nu-2)
    if nu == n-2:
        return d2
    if nu > n-1:
        d1 = deivis_sequence(n,nu-1)
        return d1
    else:
        if nu == 0:
            return 1
        elif 1 <= nu <= 2:
            return nu
        elif 2 < nu <= 3:
            s = (((nu-2)+(nu-1))-1)
            return s
        elif 4 <= nu <= 31:
            s = ((d1)+(d2))-1
            print(s)

deivis_sequence(n,nu)