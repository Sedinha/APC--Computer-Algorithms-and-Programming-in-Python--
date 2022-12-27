n = int(input())

def multiplo3(n):
    if n == 0:
        return True
    elif n == 1 or n == 2:
        return False
    else:
        return not não_multiplo3(n-3)
    
def não_multiplo3(n):
    if n==0:
        return False
    elif n==1 or n==2:
        return True
    else:
        return not multiplo3(n-3)
    
print(multiplo3(n))
print(não_multiplo3(n))
