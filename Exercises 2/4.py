N = int(input())

def nota(N):
    estrela_nula = "☆"
    estrela = "★"
    print(f"|{estrela*N}{estrela_nula*(10-N)}|")
    
nota(N)