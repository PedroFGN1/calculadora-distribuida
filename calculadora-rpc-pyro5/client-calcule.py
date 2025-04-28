import Pyro5.api

def main():
    uri = input("Digite o URI da Calculadora: ")
    calculadora = Pyro5.api.Proxy(uri)

    while True:
        print("\nOperações disponíveis:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Exponenciação")
        print("7. Sair")

        escolha = input("Escolha a operação: ")

        if escolha == '7':
            break

        if escolha in ['1', '2', '3', '4', '6']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

        if escolha == '5':
            a = float(input("Digite o número: "))

        if escolha == '1':
            print("Resultado:", calculadora.soma(a, b))
        elif escolha == '2':
            print("Resultado:", calculadora.subtracao(a, b))
        elif escolha == '3':
            print("Resultado:", calculadora.multiplicacao(a, b))
        elif escolha == '4':
            print("Resultado:", calculadora.divisao(a, b))
        elif escolha == '5':
            print("Resultado:", calculadora.raiz_quadrada(a))
        elif escolha == '6':
            print("Resultado:", calculadora.exponenciacao(a, b))
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    main()
