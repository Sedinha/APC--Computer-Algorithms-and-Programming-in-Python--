x = int(input())

def troco(x):
    x_50 = x // 50
    x_25 = x // 25
    x_10 = x // 10
    x_5 = x // 5
    x_1 = x // 1
    xn25 = ((x_25)*25 - (x_50)*50)//25
    xn10 = (x-((x_50*50)+(x_25*25)))//10
    
    if x_50 % 50 == 0:
        return x_50
    if x_25 % 25 == 0:
        return xn25
    
    print(f"{x_50} moedas de 50 centavos")
    print(f"{xn25} moedas de 25 centavos")
    print(f"{xn10} moedas de 10 centavos")


troco(x)