n = int(input())

def deivis_sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (deivis_sequence(n-1) + deivis_sequence(n-2))-1
    
print(deivis_sequence(n))