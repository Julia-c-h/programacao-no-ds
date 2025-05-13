class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}"

# Solicitação de dados ao usuário
titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
paginas = input("Digite a quantidade de páginas do livro: ")

# Criando o objeto Livro
livro = Livro(titulo, autor, paginas)

# Exibindo a descrição formatada do livro
print("\nInformações do livro cadastrado:")
print(livro)
