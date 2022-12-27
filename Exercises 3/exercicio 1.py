M = int(input())

if 0 <= M <= 60:
    if M % 2 == 0:
        print("Fome de comida! Queremos arroz e feijão")
    else:
        print("Só um lanchinho cai bem!")
else:
    print("Apenas valores entre 0 e 60 !")