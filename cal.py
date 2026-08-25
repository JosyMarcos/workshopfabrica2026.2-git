class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self):
        return self.num1 + self.num2

    def subtrair(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 == 0:
            return "Erro: divisão por zero"
        return self.num1 / self.num2


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

calc = Calculadora(n1, n2)

print("Soma:", calc.somar())
print("Subtração:", calc.subtrair())
print("Multiplicação:", calc.multiplicar())
print("Divisão:", calc.dividir())