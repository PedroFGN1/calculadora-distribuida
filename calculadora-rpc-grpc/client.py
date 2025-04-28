import grpc
import calculadora_pb2
import calculadora_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculadora_pb2_grpc.CalculadoraStub(channel)

        while True:
            print("\nOperações disponíveis:")
            print("1. Soma")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Raiz Quadrada")
            print("6. Exponenciação")
            print("7. Sair")

            opcao = input("Escolha a operação: ")

            if opcao == '7':
                break

            if opcao in ['1', '2', '3', '4', '6']:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                operacao = calculadora_pb2.OperacaoDoisNumeros(a=a, b=b)

                if opcao == '1':
                    resposta = stub.Somar(operacao)
                elif opcao == '2':
                    resposta = stub.Subtrair(operacao)
                elif opcao == '3':
                    resposta = stub.Multiplicar(operacao)
                elif opcao == '4':
                    resposta = stub.Dividir(operacao)
                elif opcao == '6':
                    resposta = stub.Exponenciar(operacao)

            elif opcao == '5':
                a = float(input("Digite o número: "))
                operacao = calculadora_pb2.OperacaoUmNumero(a=a)
                resposta = stub.RaizQuadrada(operacao)

            else:
                print("Opção inválida")
                continue

            print(f"Resultado: {resposta.resultado}")

if __name__ == '__main__':
    run()
