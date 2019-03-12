import socket
import random
#form struct import unpack
#import ison.pickle

mySock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_addr = (socket.gethostname(), 44152)
mySock.bind(listen_addr) 
data = "-941349"
#addr = ("localhost", PC5565-111-00.meca.ingenierie.upmc.fr)
addr=(socket.gethostbyname('PC5565-111-00.meca.ingenierie.upmc.fr'), 21568)

mySock.sendto(data.encode(),addr)
data = mySock.recv(1024)

print(data.decode())
