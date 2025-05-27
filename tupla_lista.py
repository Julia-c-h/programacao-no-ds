class Biblioteca:
    def __init__(self):
        self._colecao_livros = ()  # Inicializa a tupla vazia (imutável)
        self.lista_livros = []  # Lista para armazenar os dados

    def adicionar_livro(self, titulo, autor, ano):
        novo_livro = (titulo, autor, ano)  # Criando um livro como tupla
        self._colecao_livros += (novo_livro,)  # Adicionando à tupla (imutável)
        self.lista_livros.append(novo_livro)  # Atualizando a lista

    def consultar_colecao(self):
        print("Coleção de Livros (Tupla - Imutável):")
        for livro in self._colecao_livros:
            print(livro)

    def consultar_lista(self):
        print("\nLista de Livros (Atualizável):")
        for livro in self.lista_livros:
            print(livro)

# Criando uma instância da biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
biblioteca.adicionar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
biblioteca.adicionar_livro("1984", "George Orwell", 1949)

# Consultando a coleção e a lista
biblioteca.consultar_colecao()
biblioteca.consultar_lista()
