def menu():
    while True:
        print("### APC ### /n")
        print("Opções")
        print("1 - Cadastra aluno")
        print("2 - Entrada de notas")
        print("3 - Ver extrato geral")
        op = int(input("Digite o número da opção desejada: "))
        if 1 <= op <= 3:
            return op

def efetua_cadastro(cadastro):
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o Sobrenome: ")
    mat = input("Digite a Matricula: ")
    notas_le = [0.0]*11
    notas_p = [0.0]*3
    cadastro.append([nome,sobrenome,mat,notas_le,notas_p])
    
def entrada_notas(cadastro):
    if len(cadastro) == 0:
        print("Cadastre alguém !")
    else:
        matB = input("Buscar matricula: ")
        for i range(len(cadastro)):
            if cadastro[i][2] == matB:
                print(f"Entre com as notas de {cadastro[i][0]} {cadastro[i][1]}")
                
                
                


#Inicio do programa
cadastro = []
continua = "s"
while continua != "n":
    op = menu()
    
    if op == 1:
        efetua_cadastro(cadastro)
    elif op == 2:
        entrada_notas(cadastro)
    elif op == 3:
        extrato(cadastro)
    
    continua = input("Deseja continuar ? (s/n)")
    