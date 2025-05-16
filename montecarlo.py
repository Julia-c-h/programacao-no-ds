import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Número de trajetórias simuladas
retorno_medio = 0.07  # Retorno médio anual (7%)
desvio_padrao = 0.20  # Desvio padrão dos retornos (20%)
valor_inicial = 10000  # Valor inicial da carteira

# Gerar trajetórias simuladas
anos_array = np.arange(anos + 1)
trajetorias = np.zeros((simulacoes, anos + 1))
trajetorias[:, 0] = valor_inicial

for i in range(simulacoes):
    for j in range(1, anos + 1):
        retorno_aleatorio = np.random.normal(retorno_medio, desvio_padrao)
        trajetorias[i, j] = trajetorias[i, j - 1] * (1 + retorno_aleatorio)

# Plotar as simulações
plt.figure(figsize=(10, 6))
for i in range(simulacoes):
    plt.plot(anos_array, trajetorias[i], alpha=0.7)

plt.xlabel("Ano")
plt.ylabel("Valor da Carteira")
plt.title("Simulação de Monte Carlo para Investimentos em Ações")
plt.grid(True)
plt.show()
