import socket
#form struct import unpack
#import ison.pickle

mysock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = 'str_|_DOZO'
#addr = ("localhost", PC5565-111-00.meca.ingenierie.upmc.fr)
addr=('PC5565-111-00.meca.ingenierie.upmc.fr', 21567)

mysock.sendto(data.encode(),addr)
