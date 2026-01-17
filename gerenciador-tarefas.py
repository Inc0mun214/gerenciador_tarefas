def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1- Adicionar Tarefa ")
    print("2- Listar Tarefa")
    print("3- Concluir Tarefa")
    print("4- Remover Tarefa")
    print("5- Sair")

tarefas = []

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        tarefa = {
            "nome": nome,
            "concluida": False
        }
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                status = "✔" if tarefa["concluida"] else "❌"
                print(f"{i} - {tarefa['nome']} [{status}]")
    elif opcao == "3":
        indice = int(input("Digite o numero da tarefa: "))
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa concluida!")
        else:
            print("Indice invalido!")
    elif opcao == "4":
        indice = int(input("Digite o numero da tarefa: "))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa Removida🎭")
        else:
            print("Indice Invalido❌")
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida")

