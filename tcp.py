import sys
import conecTCP

ip = sys.argv[1]
porta = int(sys.argv[2])
argument = sys.argv[3]

if argument == "-C":
    Conect = conecTCP.tcp
    Clie = Conect.Cliente(ip,porta)

elif "-S" in argument:
    Conect = conecTCP.tcp
    servidor = Conect.Servidor(ip,porta)

