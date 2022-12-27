n = int(input())

def deivis_sequence(n):
    if  1 <= n <= 2:
        return n
    else:
        d1 = deivis_sequence(n-1)
        d2 = deivis_sequence(n-2)
        return (d1+d2)-1
      
print(deivis_sequence(n))