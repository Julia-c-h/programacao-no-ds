# Lista com pelo menos 8 nomes
nomes = ["Amanda", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena"]

# Solicita a letra ou sequência ao usuário
busca = input("Digite uma letra ou sequência para buscar nos nomes: ").lower()

# Filtra os nomes que contêm a sequência (ignorando maiúsculas/minúsculas)
resultado = [nome for nome in nomes if busca in nome.lower()]

# Exibe o resultado
if resultado:
    print("Nomes encontrados:")
    for nome in resultado:
        print("-", nome)
else:
    print("Nenhum nome encontrado com essa sequência.")
