s = input()
n = "1234567890"

def qt_n(s,n):
    i=0
    for numeros in s:
        if numeros in n:
            i += 1
    return i
print(qt_n(s,n))     