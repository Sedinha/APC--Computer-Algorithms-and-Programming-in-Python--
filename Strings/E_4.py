s = input()
def imparX(s):
    i=0
    nova_frase = ""
    for impar in s:
        if impar == s[(i*2)+1:(i*2)+2]:
            nova_frase += impar
            i += 1
    news = nova_frase.replace(" ","")
    return news

print(imparX(s))
            