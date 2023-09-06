#• Implemente um sistema de gerenciamento de comissões. O sistema
#terá a funcionalidade de cadastrar clientes, vendedores, vendas e
#contratos, além de calcular as comissões dos vendedores (novo ou
#antigo) e gerar relatórios sobre as vendas e comissões. O sistema
#deve apresentar um menu para escolha da operação que será
#realizada.
#• Obs: utilizar conceitos de orientação a objetos, como classes, objetos,
#encapsulamento, herança (se aplicável) e polimorfismo.
#FUNCIONALIDADES
#❖ Cadastro de Cliente:
#• Cada cliente terá um nome, endereço e informações de contato.
#• Os alunos devem criar uma classe Cliente com os atributos relevantes
#e métodos para criar e gerenciar clientes.
#❖ Cadastro de Vendedor:
#• Cada vendedor terá um nome, ID único e detalhes de contato.
#• Os alunos devem implementar uma classe Vendedor com os
#atributos necessários e métodos para lidar com os vendedores.
#FUNCIONALIDADES
#❖ Cadastro de Vendas:
#• Cada venda deve estar associada a um cliente, vendedor e contrato.
#• Uma venda incluirá informações como data da venda, valor da venda e
#status de pagamento.
#• Os alunos devem criar uma classe Venda para representar as vendas e suas
#informações.
#❖ Cadastro de Contrato:
#• Cada contrato deve conter detalhes sobre os termos e condições do
#acordo de venda.
#• Os alunos devem implementar uma classe Contrato para manter os
#detalhes dos contratos.
#FUNCIONALIDADES
#❖ Cálculo de Comissões:
#• O cálculo da comissão do vendedor será baseado no valor da
#venda e em um percentual de comissão.
#• Os alunos devem criar um método de cálculo de comissão (4% para
#vendedor antigo e 7% para novo) na classe Venda que calcula a
#comissão do vendedor.
#❖ Relatórios de Vendas e Comissões:
#• O sistema deve ser capaz de gerar relatórios de vendas e comissões.
#• Os alunos devem implementar métodos que gerem relatórios
#consolidados, mostrando detalhes das vendas, valores, comissões e
#outras informações relevantes.





class Usuario:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Contato: {self.contato}")

class Vendedor(Usuario):
    def __init__(self, nome, contato, id):
        super().__init__(nome, contato)
        self.id = id
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"ID: {self.id}")

class Cliente(Usuario):
    def __init__(self, nome, contato, endereco):
        super().__init__(nome, contato)
        self.endereco = endereco
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Endereço: {self.endereco}")

class Contrato:
    def __init__(self, detalhes):
        self.detalhes = detalhes
    def exibir_informacoes(self):
        print(f"Detalhes do Contrato: {self.detalhes}")

class Venda:
    def __init__(self, cliente, vendedor, contrato, data, valor, status_de_pagamento):
        self.cliente = cliente
        self.vendedor = vendedor
        self.contrato = contrato
        self.data = data
        self.valor = valor
        self.status_de_pagamento = status_de_pagamento
    def calcular_comissao(self):
        if self.vendedor.id > 100:
            return self.valor * 0.07
        else:
            return self.valor * 0.04
    def exibir_informacoes(self):
        self.exibir_informacoes(cliente)
        self.exibir_informacoes(vendedor)
        self.exibir_informacoes(contrato)
        print(f"Data da Venda: {self.data}")
        print(f"Valor da Venda: {self.valor}")
        print(f"Status de Pagamento: {self.status_de_pagamento}")

def criar_vendedor():
    nome = input("Digite o nome do vendedor: ")
    contato = input("Digite o contato do vendedor: ")
    id = int(input("Digite o ID do vendedor: "))
    return Vendedor(nome, contato, id)


def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    contato = input("Digite o contato do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    return Cliente(nome, contato, endereco)


def criar_contrato():
    detalhes = input("Digite os detalhes do contrato: ")
    return Contrato(detalhes)


def criar_venda(cliente, vendedor, contrato):
    data = input("Digite a data da venda: ")
    valor = float(input("Digite o valor da venda: "))
    status_pagamento = input("Digite o status de pagamento da venda: ")
    return Venda(cliente, vendedor, contrato, data, valor, status_pagamento)

def calcular_comissao(venda):
    comissao = venda.calcular_comissao()
    print(f"Comissão do vendedor: R${comissao:.2f}")

def exibir_informacoes(obj):
    obj.exibir_informacoes()


while True:
    print("\nOPÇÕES:")
    print("1 - Criar Cliente")
    print("2 - Criar Vendedor")
    print("3 - Criar Contrato")
    print("4 - Criar Venda")
    print("5 - Exibir Informações")
    print("6 - Calcular Comissão")
    print("7 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cliente = criar_cliente()
        print("Cliente registrado com sucesso!")
    elif opcao == '2':
        vendedor = criar_vendedor()
        print("Vendedor registrado com sucesso!")
    elif opcao == '3':
        contrato = criar_contrato()
        print("Contrato registrado com sucesso!")
    elif opcao == '4':
        if cliente is not None and vendedor is not None and contrato is not None:
            venda = criar_venda(cliente, vendedor, contrato)
            print("Venda criada com sucesso!")
        else:
            print("É necessário a criaçâo de um cliente, vendedor e contrato primeiro.")
    elif opcao == '5':
        if cliente is not None:
            exibir_informacoes(cliente)
        else:
            print("Nenhum cliente registrado.")
    elif opcao == '6':
        if venda is not None:
            calcular_comissao(venda)
        else:
            print("Nenhuma venda Registrada.")
    elif opcao == '7':
        break
    else:
        print("Opção inválida. Tente novamente.")

        