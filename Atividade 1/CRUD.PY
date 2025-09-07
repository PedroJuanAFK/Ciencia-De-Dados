contatos = []

def adicionar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    novo_contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    print("\n--- Lista de Contatos ---")
    for i, contato in enumerate(contatos):
        print(f"ID: {i}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
        print("-------------------------")

def atualizar_contato():
    listar_contatos()
    if not contatos:
        return

    try:
        id_contato = int(input("Digite o ID do contato que deseja atualizar: "))
        if 0 <= id_contato < len(contatos):
            print(f"Atualizando contato: {contatos[id_contato]['nome']}")
            contatos[id_contato]['nome'] = input("Novo nome: ")
            contatos[id_contato]['telefone'] = input("Novo telefone: ")
            contatos[id_contato]['email'] = input("Novo e-mail: ")
            print("Contato atualizado com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o ID.")

def excluir_contato():
    listar_contatos()
    if not contatos:
        return

    try:
        id_contato = int(input("Digite o ID do contato que deseja excluir: "))
        if 0 <= id_contato < len(contatos):
            contato_removido = contatos.pop(id_contato)
            print(f"Contato de '{contato_removido['nome']}' removido com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o ID.")

def menu():
    while True:
        print("\n--- Gerenciador de Contatos ---")
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Atualizar Contato")
        print("4 - Excluir Contato")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            listar_contatos()
        elif escolha == '3':
            atualizar_contato()
        elif escolha == '4':
            excluir_contato()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu()