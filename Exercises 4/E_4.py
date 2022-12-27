a,b,c = map(int,input().split())

def max2(a,b):
    if a>b:
        return a
    else:
        return b
    
def max3(a,b,c):
    if max2(a,c) and max2(b,c) > max2(a,b):
        if max2(a,c) > max2(b,c):
            return max2(a,c)
        else:
            return max2(b,c)
    else:
        return max2(a,b)
    
print(max3(a,b,c))
    
    