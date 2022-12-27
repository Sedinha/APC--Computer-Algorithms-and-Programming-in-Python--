a = 32
b = 26

def mdc(a, b):
    if b == 0:
        return a
    else:
        a = a%b
        return mdc(b,a)
    
    
print(mdc(a,b))