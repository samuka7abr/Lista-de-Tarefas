def add_tar(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return

def ver_tar(tarefas):
    print("\nLista de Tarefas")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]  
        print(f"{indice}. [{status}] {nome_tarefa}")

def att_tar(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajust = indice_tarefa - 1
    if 0 <= indice_tarefa_ajust < len(tarefas):
        tarefas[indice_tarefa_ajust]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para '{novo_nome_tarefa}'")
    else:
        print("Índice de tarefa inválido.")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajust = indice_tarefa - 1
    if 0 <= indice_tarefa_ajust < len(tarefas):
        tarefas[indice_tarefa_ajust]["completada"] = True
        print(f"Tarefa {indice_tarefa} completada com sucesso")
    else:
        print("Índice de tarefa inválido.")
    return

tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        nome_tarefa = input("Digite o Nome da Tarefa: ")
        add_tar(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tar(tarefas)
    elif escolha == "3":
        ver_tar(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        att_tar(tarefas, indice_tarefa, novo_nome_tarefa)
    elif escolha == "4":
        ver_tar(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        tarefas = [tarefa for tarefa in tarefas if not tarefa["completada"]]
        print("Tarefas completadas foram deletadas.")
    elif escolha == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")
