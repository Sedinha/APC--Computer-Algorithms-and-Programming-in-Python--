Fz = input()

def rec(F):
    d = {} 
    for c in F:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in sorted(d):            
        if c == "d" or c == "v" or c == "t":
                print(c,d[c])
        
rec(Fz)
