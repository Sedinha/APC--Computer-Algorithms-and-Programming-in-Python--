from statistics import median_grouped


def menu():
    opções = {"1" : "Cadastra aluno",
              "2" : "Entrada de Notas",
              "3" : "Dados do Aluno",
              "4" : "Ver extrato geral",}
    while True:
        print("\n#### APC ####\nOpções: ")
        for opção, descrição in sorted(opções.items()):
            print(f"{opção} - {descrição}")
        opção = input("\nDigite o numero da opção desejada: ")
            
        if opção in opções:
            return opção
            
def efetua_cadastro(cadastro):
    matricula = input("Digite sua matricula na UnB:")
    registra = True
    if matricula in cadastro:
        if input("f{registro['nome']} ja está cadastrado.\nVocê deseja sobrescrever (s/n)?") == "n":
            registra = False
    if registra:
        cadastro[matricula] = {'nome':input("Digite o seu nome completo"),
                               'listas':[0.0] * NUM_LISTAS,
                               "projetos":[0.0]* NUM_PROJETOS}
def entrada_notas(cadastro):
    if cadastro:
        matricula = input("Buscar pela matricula")
        if matricula in cadastro:
            registro = cadastro[matricula]
            print(f"Entre com as notas de {registro['nome']}:")
            registro['listas'] = [float(input(f"lista {nota_le +1}: ")) for nota_le in range(NUM_LISTAS)]
            registro['projetos'] = [float(input(f"Projeto {nota_p +1}: ")) for nota_p in range(NUM_PROJETOS)]
        else:
            print(f"A matricula {matricula} não foi encontrada.")
    else:
        print("Voce precisa cadastrar um aluno primeiro!")
        
def imprime_registro(matricula,registro):
    aluno = f"{matricula} - {registro['nome']}"
    print("#" *(len(aluno) +4))
    print(f"# {aluno} #")
    print("#" *(len(aluno) +4))
    
    for i,nota_le in enumerate(registro['lista']):
        print(f"Lista {i +1} \t({nota_le:.1f})")
    for i,nota_p in enumerate(registro['projetos']):
        print(f"Projeto {i +1} \t({nota_p:.1f})")
        
def registro(cadastro):
    if cadastro:
        matricula = input("Buscar pela matricula: ")
        if matricula in cadastro:
            imprime_registro(matricula,cadastro[matricula])
        else:
            print(f"A matricula {matricula} não foi encontrada!")
    else:
        print("Voce precisa cadastrar alguem antes")
        
def media(lista):
    return sum(lista)/len(lista)

def nota_final(nota_le,nota_p):
    nota_final = (0.4*nota_le) + (0.6*nota_p)
    if nota_le < 5.0 or nota_p < 5.0:
        nota_final = min (nota_final,4.9)
    return nota_final

def extrato(cadastro):
    "Mostra todas as notas,medias,e a nota final de cada aluno"
    for matricula in cadastro:
        registro = cadastro[matricula]
        imprime_registro(matricula,registro)
        
        media_le = media(registro['listas'])
        media_p = media(registro['projetos'])
        n_final = nota_final(media_le,media_p)
        print(f'LE = {media_le:.1f}')
        print(f"P = {media_p:.1f}")
        print(f"NF ={n_final:.1f}")
# INICIO DO PROGRAMA #
cadastro = {}

#constantes globais#
NUM_LISTAS = 11
NUM_PROJETOS = 3

continua = 's'
while continua != 'n':
    op = menu()
    
    if op == "1":
        efetua_cadastro(cadastro)
    elif op == "2":
        entrada_notas(cadastro)
    elif op == "3":
        registro(cadastro)
    elif op == "4":
        extrato(cadastro)
    
    continua = input('Deseja continuar ? (s/n)') 