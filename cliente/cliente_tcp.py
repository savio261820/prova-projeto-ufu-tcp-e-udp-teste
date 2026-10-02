import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("10.0.99.150", 1213))

print("Conectado ao servidor")

while True:
    mensagem = input("Digite uma mensagem ou operação: ")

    if mensagem == "sair":
        break

    cliente.send(mensagem.encode())

    resposta = cliente.recv(1024).decode()

    print("Servidor:", resposta)

cliente.close()