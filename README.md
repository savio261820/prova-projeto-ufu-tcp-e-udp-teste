# Cliente-Servidor com TCP e UDP

Projeto desenvolvido para a atividade de programação de sockets da disciplina de Cibersegurança da Universidade Federal de Uberlândia.

O objetivo é demonstrar, de forma simples, a comunicação entre cliente e servidor utilizando os protocolos TCP e UDP através da biblioteca `socket` do Python.

A aplicação permite o envio de mensagens de texto e também de operações matemáticas básicas do cliente para o servidor.

## Estrutura do projeto

```text
.
├── README.md
│
├── clientes/
│   ├── menu.py
│   ├── cliente_tcp.py
│   └── cliente_udp.py
│
└── servidor/
    ├── servidor_tcp.py
    └── servidor_udp.py
