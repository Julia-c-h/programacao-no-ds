# Solicita ao usuário as coordenadas geográficas
coordenadas = input("Digite a latitude e longitude separadas por vírgula: ")

# Converte os valores em uma tupla e desempacota
latitude, longitude = map(float, coordenadas.split(','))

# Exibe os valores
print(f"\nCoordenadas Geográficas:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
