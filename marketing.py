def calcular_engajamento_seguidores(curtidas, comentarios, compartilhamentos, seguidores):
    return (curtidas + comentarios + compartilhamentos) / seguidores * 100

def calcular_engajamento_alcance(curtidas, comentarios, compartilhamentos, alcance):
    return (curtidas + comentarios + compartilhamentos) / alcance * 100

def calcular_engajamento_impressoes(curtidas, comentarios, compartilhamentos, impressoes):
    return (curtidas + comentarios + compartilhamentos) / impressoes * 100

# Solicitar os dados ao usuário
curtidas = int(input("Digite o número de curtidas: "))
comentarios = int(input("Digite o número de comentários: "))
compartilhamentos = int(input("Digite o número de compartilhamentos: "))
seguidores = int(input("Digite o número de seguidores: "))
alcance = int(input("Digite o alcance da publicação: "))
impressoes = int(input("Digite o número de impressões: "))

# Calcular e exibir os resultados
print("\nEngajamento por seguidores: {:.2f}%".format(calcular_engajamento_seguidores(curtidas, comentarios, compartilhamentos, seguidores)))
print("Engajamento por alcance: {:.2f}%".format(calcular_engajamento_alcance(curtidas, comentarios, compartilhamentos, alcance)))
print("Engajamento por impressões: {:.2f}%".format(calcular_engajamento_impressoes(curtidas, comentarios, compartilhamentos, impressoes)))
