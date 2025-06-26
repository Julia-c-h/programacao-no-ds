# Lista pré-definida de títulos de livros
livros = [
    "Dom Casmurro",
    "O Pequeno Príncipe",
    "Cem Anos de Solidão",
    "A Menina que Roubava Livros",
    "1984",
    "O Senhor dos Anéis",
    "Grande Sertão: Veredas",
    "Capitães da Areia",
    "Harry Potter e a Pedra Filosofal",
    "A Revolução dos Bichos"
]

# Solicita ao usuário uma palavra-chave ou sequência de caracteres
busca = input("Digite uma palavra-chave ou parte do título: ").lower()

# Filtra os títulos com base na busca, ignorando maiúsculas/minúsculas
resultados = [livro for livro in livros if busca in livro.lower()]

# Exibe os resultados
if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print(f"- {titulo}")
else:
    print("\nNenhum título encontrado com esse critério.")
