a = float(input())
b = float(input())
c = float(input())
#-----------------------------------------------------------------------------
def calcula_delta():
    (b**2) - (4*a*c)
    
def calcula_x1():
    ((-b)+(delta**(1/2)))/(2*a)
    
def calcula_x2():
    ((-b)-(delta**(1/2)))/(2*a)


def calcula_raizes():
    delta = calcula_delta()
    
    if delta < 0:
        print("Não há raizes reais!")
    
    if delta == 0:
        x = calcula_x1()
        print(f"x = {x}")
    
    if delta > 0:
        x1 = calcula_x1()
        x2 = calcula_x2()
        print(f" x'1 = {x1}, x'2 = {x2}")

calcula_raizes()
        