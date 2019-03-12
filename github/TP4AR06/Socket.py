import socket
from struct import pack

mysock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#data2 = 'str_|_DOZO'
#addr = ("localhost", PC5565-111-00.meca.ingenierie.upmc.fr)

addr=('134.157.103.149', 21560)
# ip Sinan 134.157.104.149
#data = 'dd'
#mysock.sendto(data.encode,addr)
data = pack("3si3s", "SI ".encode(), 16, "NAN".encode())
mysock.sendto(data,addr)
