import socket
#form struct import unpack
#import ison.pickle

mychaussette = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = 'int_|_156'
#addr = ("localhost", PC5565-111-00.meca.ingenierie.upmc.fr)
addr=('PC5565-111-00.meca.ingenierie.upmc.fr', 21568)

mychaussette.sendto(data.encode(),addr)
mychaussette.recv(21568)

print("answer:", mychaussette)
