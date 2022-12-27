def calcula_distancia(x,y,xc,yc):
    def mod(z1,z2):
        if z2 - z1 > 0:
            return z2 - z1
        else:
            return -(z2 - z1)
    return mod(xc,x) + mod(yc,y)

calcula_distancia(x,y,xc,yc)