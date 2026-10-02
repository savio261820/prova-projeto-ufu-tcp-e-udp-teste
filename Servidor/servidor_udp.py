import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(("0.0.0.0", 1213))

print("Servidor UDP iniciado na porta 1213")

while True:
    mensagem, endereco = servidor.recvfrom(1024)

    mensagem = mensagem.decode()
    mensagem_sem_espaco = mensagem.replace(" ", "")

    print("Recebido:", mensagem)

    try:
        if "+" in mensagem_sem_espaco:
            numeros = mensagem_sem_espaco.split("+")
            resultado = float(numeros[0]) + float(numeros[1])
            resposta = str(resultado)

        elif "-" in mensagem_sem_espaco:
            numeros = mensagem_sem_espaco.split("-")
            resultado = float(numeros[0]) - float(numeros[1])
            resposta = str(resultado)

        elif "*" in mensagem_sem_espaco:
            numeros = mensagem_sem_espaco.split("*")
            resultado = float(numeros[0]) * float(numeros[1])
            resposta = str(resultado)

        elif "/" in mensagem_sem_espaco:
            numeros = mensagem_sem_espaco.split("/")

            if float(numeros[1]) == 0:
                resposta = "Erro: não é possível dividir por zero."
            else:
                resultado = float(numeros[0]) / float(numeros[1])
                resposta = str(resultado)

        else:
            resposta = 'Sua mensagem "' + mensagem + '" foi recebida no servidor.'

    except:
        resposta = 'Sua mensagem "' + mensagem + '" foi recebida no servidor.'

    servidor.sendto(resposta.encode(), endereco)

    print("Resposta:", resposta)
