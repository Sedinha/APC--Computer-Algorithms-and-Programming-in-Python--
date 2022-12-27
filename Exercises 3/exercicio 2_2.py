def tutoria():
    print("Já foi na tutoria?")
    answer = input()
    if answer == "SIM":
            print("Choremos!")
    elif answer == "NÃO":
            print("Temos um time a disposição!")

print("O programa funciona?")
answer = input()

if answer  == "SIM":
    print("Você entende o que fez?")
    answer = input()
    if answer == "SIM":
        print("Ótimo. Então não mexe!")
    elif answer == "NÃO":
        tutoria()

elif answer == "NÃO":
    print("Você sabe onde está o erro?")
    answer = input()
    if answer == "SIM":
        print("Acha que pode solucionar sozinho?")
        answer = input()
        if answer == "SIM":
            print("Então mão na massa!")
        elif answer == "NÃO":
            print("Já pesquisou no Google?")
            if answer == "SIM":
                tutoria()
    elif answer == "NÃO":
        tutoria()