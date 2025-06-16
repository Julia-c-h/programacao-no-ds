# 1. Lista de nomes de estudantes
estudantes = ["Carlos", "Ana", "Pedro", "Beatriz", "Mariana"]

# Ordena diretamente a lista original em ordem decrescente
estudantes.sort(reverse=True)
print("Estudantes ordenados (decrescente):", estudantes)  # Agora a lista estará em ordem decrescente

# Lista com notas
lista_original = [3, 1, 4, 1, 5, 9, 2, 6]

# Use sorted() para ordenar em ordem crescente (padrão)
lista_crescente = sorted(lista_original)
print("Lista em ordem crescente:", lista_crescente)

# Use sorted() para ordenar em ordem decrescente
lista_decrescente = sorted(lista_original, reverse=True)
print("Lista em ordem decrescente:", lista_decrescente)  

# A lista original permanece inalterada
print("Lista original:", lista_original)  
