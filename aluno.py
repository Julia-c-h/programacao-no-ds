import functools

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):
    return (a.nota > b.nota) - (a.nota < b.nota)

# Coletando informações dos alunos
alunos = []
for i in range(3):
    nome = input(f'Informe o nome do aluno {i+1}: ')
    nota = int(input(f'Informe a nota do aluno {i+1}: '))
    alunos.append(Aluno(nome, nota))

# Ordenando a lista de alunos
alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))

print(alunos_ordenados)
