class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

# Chamando os métodos estáticos sem instanciar a classe
print("Soma:", Calculadora.somar(10, 5))
print("Subtração:", Calculadora.subtrair(10, 5))
