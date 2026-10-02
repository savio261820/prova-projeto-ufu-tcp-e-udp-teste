import os

print("Selecione o protocolo")
print("---------------------")
print("\n")
print("1. TCP")
print("2. UDP")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    os.system("python3 cliente_tcp.py")

elif opcao == "2":
    os.system("python3 cliente_udp.py")

else:
    print("Opção inválida.")