class Hotelaria:
    _id_counter = 1

    def __init__(self, nome, endereco, cidade, estado, telefone):
        self.id = Hotelaria._id_counter
        Hotelaria._id_counter += 1
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone

    def __str__(self):
        return f"[ID: {self.id}] Nome: {self.nome}, Endereço: {self.endereco}, Cidade: {self.cidade}, Estado: {self.estado}, Telefone: {self.telefone}"


class Quarto:
    _id_counter = 1

    def __init__(self, numero, preco):
        self.id = Quarto._id_counter
        Quarto._id_counter += 1
        self.numero = numero
        self.preco = preco

    def __str__(self):
        return f"[ID: {self.id}] Quarto {self.numero}, Preço: R$ {self.preco:.2f}"


clientes = []
quartos = []


def menu_hotelaria():
    while True:
        print("\n=== Menu Hotelaria ===")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Cadastrar Quarto")
        print("4 - Listar Quartos")
        print("5 - Sair")

        try:
            opcao = int(input("\nDigite a opção: "))
            if opcao == 1:
                cadastrar_cliente()
            elif opcao == 2:
                listar_clientes()
            elif opcao == 3:
                cadastrar_quarto()
            elif opcao == 4:
                listar_quartos()
            elif opcao == 5:
                print("\nSaindo do sistema. Até logo!")
                break
            else:
                print("\nOpção inválida!")
        except ValueError:
            print("\nOpção inválida! Digite um número inteiro.")


def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    telefone = input("Telefone: ")
    cliente = Hotelaria(nome, endereco, cidade, estado, telefone)
    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")


def listar_clientes():
    print("\n--- Lista de Clientes ---")
    if not clientes:
        print("Nenhum cliente cadastrado ainda.")
    else:
        for cliente in clientes:
            print(cliente)


def cadastrar_quarto():
    print("\n--- Cadastro de Quarto ---")
    numero = input("Número do quarto: ")
    try:
        preco = float(input("Preço: "))
        quarto = Quarto(numero, preco)
        quartos.append(quarto)
        print("\nQuarto cadastrado com sucesso!")
    except ValueError:
        print("\nPreço inválido! Insira um número válido.")


def listar_quartos():
    print("\n--- Lista de Quartos ---")
    if not quartos:
        print("Nenhum quarto cadastrado ainda.")
    else:
        for quarto in quartos:
            print(quarto)


# Programa principal
menu_hotelaria()

            