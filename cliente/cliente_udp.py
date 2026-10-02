import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem = input("Digite uma mensagem ou operação: ")

    if mensagem == "sair":
        break

    cliente.sendto(mensagem.encode(), ("10.0.99.150", 1213))

    resposta, endereco = cliente.recvfrom(1024)

    print("Servidor:", resposta.decode())

cliente.close()