import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("0.0.0.0", 1213))

servidor.listen(1)

print("Servidor TCP iniciado na porta 1213")
print("Esperando cliente...")

conexao, endereco = servidor.accept()

print("Cliente conectado:", endereco)

while True:
    mensagem = conexao.recv(1024).decode()

    if mensagem == "":
        break

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

    if resposta.endswith(".0"):
        resposta = resposta[:-2]

    conexao.send(resposta.encode())

    print("Resposta:", resposta)

conexao.close()
servidor.close()
