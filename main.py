from aluno import AdicionarAluno, RemoverAluno, AtualizarAluno, VerAlunos

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            AdicionarAluno()
        elif opcao == "2":
            RemoverAluno()
        elif opcao == "3":
            AtualizarAluno()
        elif opcao == "4":
            VerAlunos()
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
