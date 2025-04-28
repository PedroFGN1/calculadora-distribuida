import grpc # Importado para o uso de gRPC / Comunicação entre cliente e servidor
from concurrent import futures # Incorporado para o uso de múltiplas threads / Concorrência
import time # Importado para o uso de sleep / Legibilidade e Debugging
import calculadora_pb2 # Importado para o uso de mensagens e tipos definidos no arquivo .proto / Serialização e Deserialização de dados
import calculadora_pb2_grpc # Importado para o uso de serviços definidos no arquivo .proto / Implementação do gRPC, Stubs e Servidores
import math # Importado para o uso de funções matemáticas / Cálculos matemáticos

class CalculadoraServicer(calculadora_pb2_grpc.CalculadoraServicer):

    def Somar(self, request, context): # O context é usado para definir o status da operação / O request é o objeto que contém os dados enviados pelo cliente
        return calculadora_pb2.Resultado(resultado=request.a + request.b)

    def Subtrair(self, request, context):
        return calculadora_pb2.Resultado(resultado=request.a - request.b)

    def Multiplicar(self, request, context):
        return calculadora_pb2.Resultado(resultado=request.a * request.b)

    def Dividir(self, request, context):
        if request.b == 0:
            context.set_details('Divisão por zero')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT) 
            return calculadora_pb2.Resultado()
        return calculadora_pb2.Resultado(resultado=request.a / request.b)

    def RaizQuadrada(self, request, context):
        return calculadora_pb2.Resultado(resultado=math.sqrt(request.a))

    def Exponenciar(self, request, context): 
        return calculadora_pb2.Resultado(resultado=math.pow(request.a, request.b))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraServicer(), server) # Adiciona o servicer ao servidor gRPC
    server.add_insecure_port('[::]:50051') # Adiciona uma porta para o servidor gRPC
    server.start()
    print("Conectando ao servidor...")
    time.sleep(1)  # Aguarda um segundo para garantir que o servidor esteja pronto
    print(f"Servidor rodando na porta 50051..."+ f"Conexão estabelecida em: " + time.strftime("%d-%m-%Y ás %H:%M:%S")) # Formato de data e hora
    print("Pressione Ctrl+C para parar o servidor.")
    try:
        while True:
            time.sleep(86400)  # Sleep for a day
    except KeyboardInterrupt:
        print("Servidor parando...")
    finally:
        server.stop(0)
        print("Servidor parado.")
    server.wait_for_termination() # Aguarda a finalização do servidor

if __name__ == '__main__':
    serve()
