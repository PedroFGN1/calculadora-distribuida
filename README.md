# 🧮 Calculadoras Distribuídas em Python

Desenvolvido como parte de uma atividade da disciplina de Sistemas Distribuídos, com foco em comparar abordagens de RPC em Python.

Este repositório contém duas implementações de uma **calculadora distribuída**, que permite realizar operações matemáticas remotamente através de duas abordagens diferentes:

- **Pyro5** – Simples e nativa para aplicações Python.
- **gRPC** – Robusta, performática e compatível com múltiplas linguagens.

---

## 🚀 Funcionalidades

Ambas as calculadoras implementam as seguintes operações matemáticas:

1. Soma (`a + b`)
2. Subtração (`a - b`)
3. Multiplicação (`a * b`)
4. Divisão (`a / b`)
5. Raiz quadrada (`√a`)
6. Exponenciação (`base^expoente`)

---

## ▶️ Como Executar

### 📌 Pyro5

1. Instale as dependências:
   ```bash
    pip install Pyro5
2. Iniciar o Name Server:
   ```bash 
    python -m Pyro5.nameserver
3. Em outros Terminais, Executar Cliente e Servidor:
   ```bash
    python servidor.py
    python cliente.py

### 📌 gRPC

1. Instale as dependências:
    ```bash
    pip install grpcio grpcio-tools

2. Gere os arquivos a partir do .proto:
    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto

3. Execute o servidor e o cliente:
    ```bash
    python servidor.py
    python cliente.py

📄 Licença
Este projeto está licenciado sob os termos da MIT License.