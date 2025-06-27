# Lista de cidades
cidades = ["Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte", 
           "Salvador", "Porto Alegre", "Manaus", "Recife"]

# Solicita ao usuário um termo de busca
busca = input("Digite uma letra ou sequência de caracteres para buscar: ").lower()

# Filtra as cidades que contêm o termo, ignorando maiúsculas/minúsculas
cidades_filtradas = [cidade for cidade in cidades if busca in cidade.lower()]

# Exibe o resultado
if cidades_filtradas:
    print("Cidades encontradas:")
    for cidade in cidades_filtradas:
        print(f"- {cidade}")
else:
    print("Nenhuma cidade corresponde ao critério de busca.")
