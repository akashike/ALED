import socket
import random

# Création d'un socket UDP (SOCK_DGRAM)
UDPSock = socket.socket(type=socket.SOCK_DGRAM)
# Ecoute sur port 21567 à tous les IPs
# Attention si vous n'etes pas derriere une firewall, vous accepter TOUT LE MONDE
# C'est comme poster sa fete sur facebook en public...
listen_addr = (socket.gethostname(), 21568)
UDPSock.bind(listen_addr)

print(f"Setting UDP host {listen_addr}")

allDict = {}

while True:
    # On attend un paquet de taille 1024 octets max

    data, addr = UDPSock.recvfrom(4096)
    try:
        thisInt = allDict[addr]
    except KeyError:
        thisInt[addr] = random.randint(-1000000, 1000000)

    try:
        intGuess = int(data.decode())
    except:
        UDPSock.sendto(b"-1", addr)
    if intGuess < thisInt:
        UDPSock.sendto(b"1", addr)
    elif intGuess < thisInt:
        UDPSock.sendto(b"2", addr)
    else:
        UDPSock.sendto(b"0", addr)
        allDict.pop(addr)
