import Pyro5.api

@Pyro5.api.expose
class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            return "Erro: divisão por zero"
        return a / b

    def raiz_quadrada(self, a):
        if a < 0:
            return "Erro: número negativo"
        return a ** 0.5

    def exponenciacao(self, base, expoente):
        return base ** expoente

def main():
    daemon = Pyro5.api.Daemon()
    uri = daemon.register(Calculadora)
    print("Objeto Calculadora disponível. URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
