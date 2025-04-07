palavra_secreta = "girafa".lower()  # Torna a palavra secreta consistente em letras minúsculas
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6
desenho_forca = [
    "  O  ",  # Cabeça
    "  |  ",  # Tronco
    " /|\\ ", # Braços
    " / \\ ", # Pernas
    "===== ", # Base
]

print("Bem-vindo ao jogo da forca! Você tem 6 tentativas.\n")

while tentativas > 0 and "_" in letras_acertadas:
    print("Forca:")
    for parte in desenho_forca[:6 - tentativas]:
        print(parte)
    
    print("\nPalavra:", " ".join(letras_acertadas))
    palpite = input("Digite uma letra: ").lower()
    
    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, insira apenas uma única letra válida.")
        continue
    
    if palpite in palavra_secreta:
        indices = [i for i, letra in enumerate(palavra_secreta) if letra == palpite]
        for i in indices:
            letras_acertadas[i] = palpite
        print("Você acertou uma letra!")
    else:
        tentativas -= 1
        print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
    
    print("\n")

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, você perdeu. A palavra era:", palavra_secreta)
    print("\nForca final:")
    for parte in desenho_forca:
        print(parte)
