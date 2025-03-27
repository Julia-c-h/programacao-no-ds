#include <stdio.h>

int main() {
    int num1, num2, soma;

    // Solicita a entrada dos números ao usuário
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);

    printf("Digite o segundo número: ");
    scanf("%d", &num2);

    // Realiza a soma
    soma = num1 + num2;

    // Exibe o resultado
    printf("A soma de %d e %d é: %d\n", num1, num2