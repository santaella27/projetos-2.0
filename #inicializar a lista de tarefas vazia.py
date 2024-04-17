#inicializar a lista de tarefas vazia 
tasks = []

def add_task(task):
    tasks.append(task)
    print("Tarefa adicionada com sucesso")

def list_tasks():
    if tasks:
        print("Lista de Tarefas:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("A lista de tarefas está vazia.")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Tarefa '{removed_task}' removida com sucesso!")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("\nO que você gostaria de fazer?")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            task = input("Digite a tarefa: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Digite o índice da tarefa a ser removida: "))
            remove_task(index)
        elif choice == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()



