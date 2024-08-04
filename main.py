# Classe de criação dos elementos da lista - Trabalho de Geovanna Melo
class Estados:

    def __init__(self, sigla=None, nomeEstado=None):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

# Classe de criação da lista encadeada simples
class ListaEstados:
    def __init__(self):
        self.head = None

    def inserir(self, sigla, nomeEstado):
        nodo = Estados(sigla, nomeEstado)

        if self.head == None:
            self.head = nodo
            return 0

        else:
            nodo.proximo = self.head
            self.head = nodo
            return 0

    def imprimir(self):
        temp = self.head
        while temp:
            print(f"{temp.sigla} -> ", end="")
            temp = temp.proximo
        print("None")

# Classe de criação da tabela hash
class TabelaHash:

    def __init__(self):
        self.tam = 10
        self.h = [ListaEstados() for i in range(0, self.tam)]

    def hashFunc(self, sigla):
        if sigla == "DF":
            return 7
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % self.tam

    def inserir(self, sigla, nomeEstado):
        pos = self.hashFunc(sigla)
        self.h[pos].inserir(sigla, nomeEstado)

    def imprimir(self):
        for i in range(0, self.tam):
            print(f"{i}:", end="")
            self.h[i].imprimir()

# Chama o programa principal
Programa = TabelaHash()
while True:
    print('MENU:')
    print('1 - Inserir na tabela hash')
    print('2 - Listar tabela hash')
    print('3 - Sair')

# Lê as opçoes digitadas pelo usuario
    op = int(input("Escolha uma opção:"))
    if op == 1:
        sigla = input('Digite a sigla do estado:')
        nomeEstado = input('Digite o nome do estado:')
        Programa.inserir(sigla, nomeEstado)
    elif op == 2:
        Programa.imprimir()
    elif op == 3:
        print('Encerrando o programa.')
        break
    else:
        print("Opção inválida, tente novamente.")