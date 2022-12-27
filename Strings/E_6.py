def censura(tt,cen):
    ttS = tt.split(" ")
    if not cen in ttS:
        return "tudo certo :)"

    for w in ttS:
        if w in cen:
            tt = tt.replace(cen,"*")
    return tt

tt = input()
cen = input()

print(censura(tt,cen))
    