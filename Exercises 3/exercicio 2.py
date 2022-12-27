def google():
    print("Você ja pesquisou no Google?")
    answer = input()
    if answer == "SIM":
        tutoria()
    else:
        print("Corre lá então!")

def tutoria():
    print("Já foi na tutoria?")
    answer = input()
    if answer == "SIM":
            print("Choremos!")
    else:
            print("Temos um time a disposição!")

print("O programa funciona?")
answer = input()

if answer  == "SIM":
    print("Você entende o que fez?")
    answer = input()
    if answer == "SIM":
        print("Ótimo. Então não mexe!")
    else:
        tutoria()

else:
    print("Você sabe onde está o erro?")
    answer = input()
    if answer == "SIM":
        print("Acha que pode solucionar sozinho?")
        answer = input()
        if answer == "SIM":
            print("Então mão na massa!")
        else:
            google()
    else:
        tutoria()