ext = input()
extS = ext.split(" ")
extenso = "um,dois,três,quatro,cinco,seis,sete,oito,nove"
num = "1,2,3,4,5,6,7,8,9"
numS = num.split(",")
extensoS = extenso.split(",")

def trocaExt(extS,extensoS,numS):
    i = 0
    frase = ""
    for n in extS:
        if n in extensoS:
            n = n.replace(extensoS == "cinco" ,numS[i])
            frase += n
        else:
            frase+= extS[i]
        i += 1
            
print(trocaExt(extS,extensoS,numS))
            