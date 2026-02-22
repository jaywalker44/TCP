#!/user/bin/python3

import os
import socket
import time
import sys

class tcp:
    def Servidor(ipc,porta):
        Server_Conect = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        #Hospedagem Do IP & PORTA
        Server_Conect.bind((ipc,porta))
        Server_Conect.listen(1)
        print(f"~Aguardando a conexão na porta {porta}")
        Conect , ip = Server_Conect.accept()

        #Agora Vamos No Loop
        print(f"~Cliente conectado com sucesso {ip}")
        while True:
            msg = str(input("[~EU] >_ "))
            Conect.send(msg.encode())
            msg1 = Conect.recv(1024)
            print(f"[~Cliente] >_ {msg1.decode()}")
            if "SAIR" in msg1.decode():
                sys.exit(0)
                Server_Conect.close()

    def Cliente(ip,porta):
        sms = """Programa Desenvolvido Pelo jaywalker [João Norton Muzadi] : se gostou , siga me no  GitHUB"""
        Client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        print(f"~Conectando ao servidor >_ {ip}")
        Client.connect((ip,porta))
        print(f"{sms}")
        time.sleep(2)
        os.system("clear")
        print(f"~Cliente Conectado ao servidor {ip} com sucesso !")
        time.sleep(2)

        while True:
            msg1 = Client.recv(1024)
            print(f"[~Servidor] >_ {msg1.decode()}")
            msg = str(input(f"[~EU] >_ "))
            Client.send(msg.encode())
            if "SAIR" in msg1.decode():
                sys.exit(0)
                Client.close()

#FIM - - - - - - - - - - - - - 
