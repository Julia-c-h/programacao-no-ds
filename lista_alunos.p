# Lista de alunos: cada aluno é representado por um dicionário com nome e nota
alunos = [
    {"nome": "Carlos", "nota": 85},
    {"nome": "Ana", "nota": 92},
    {"nome": "Bruno", "nota": 78},
    {"nome": "Daniela", "nota": 95}
]

# Ordenando por nome (modifica a lista original)
alunos.sort(key=lambda aluno: aluno["nome"])  

print("Lista de alunos ordenada por nome:")
for aluno in alunos:
    print(aluno)

# Ordenando por nota em ordem decrescente (cria uma nova lista)
alunos_por_nota = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)

print("\nLista de alunos ordenada por nota (decrescente):")
for aluno in alunos_por_nota:
    print(aluno)
