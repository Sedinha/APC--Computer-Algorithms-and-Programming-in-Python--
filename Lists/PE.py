L = [1546,1564,1646,1705,1618,1755,1609,1655,1509,1828,1546,1614,1646,1464,1691,1473,1446,1637,1537,1682]
lL = len(L)

def calc_dp(L):
    i=0
    n = len(L)
    r2 = 0
    m = 0    
    for n1 in L:
        m += n1
    m = m/n
    while i < len(L):
        r1 = (L[i]-m)**2
        r2 += r1
        i += 1
    r3 = r2/(n-1)
    return print(f"{(r3)**(1/2)} e {m}")
        
calc_dp(L)