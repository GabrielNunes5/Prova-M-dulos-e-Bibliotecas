# Dicionário para armazenar os alunos
alunos = {1: "Gabriel"}

def AdicionarAluno():
    matricula = int(input("Digite o número de matrícula do aluno: "))
    nome = input("Digite o nome do aluno: ")

    if matricula in alunos:
        print("Erro: Matrícula já existente.")
        print("-"*50)
    else:
        alunos[matricula] = nome
        print(f"Aluno {nome} adicionado com sucesso.")
        print("-"*50)

def RemoverAluno():
    matricula = int(input("Digite o número de matrícula do aluno a ser removido: "))
    
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno {nome} removido com sucesso.")
        print("-"*50)
    else:
        print("Erro: Matrícula não encontrada.")
        print("-"*50)

def AtualizarAluno():
    matricula = int(input("Digite o número de matrícula do aluno a ser atualizado: "))
    
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print(f"Aluno {matricula} atualizado para {novo_nome}.")
        print("-"*50)
    else:
        print("Erro: Matrícula não encontrada.")
        print("-"*50)

def VerAlunos():
    if alunos:
        print("Lista de Alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula} - Nome: {nome}")
        print("-"*50)
    else:
        print("Nenhum aluno cadastrado.")
        print("-"*50)
