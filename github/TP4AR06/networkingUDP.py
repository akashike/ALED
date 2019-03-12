import socket
from struct import unpack
import json,pickle

# Création d'un socket UDP (SOCK_DGRAM)
UDPSock = socket.socket(type=socket.SOCK_DGRAM)
# Ecoute sur port 21567 à tous les IPs
# Attention si vous n'etes pas derriere une firewall, vous accepter TOUT LE MONDE
# C'est comme poster sa fete sur facebook en public...
listen_addr = (socket.gethostname(), 21567)
UDPSock.bind(listen_addr)

print(f"Setting UDP host {listen_addr}")

while True:
    # On attend un paquet de taille 1024 octets max

    data, addr = UDPSock.recvfrom(1024)

    if len(data) < 9:
        print(f"Message de {addr} et trop courte")
        continue

    #On attend le format "format_|_MSG
    fmtTokenized = data[:9].decode().split("_|_")

    if len(fmtTokenized) != 2:
        print(f"{addr} a envoyé n'importe quoi comme format du string binaire")
        continue

    if fmtTokenized[0] not in ["str", "json", "pickle", "pack"]:
        print(f"{addr} a envoyé n'importe quoi comme format")
        continue

    fmtTokenized = fmtTokenized[0]
    msgB = data[len(fmtTokenized) + 3:]

    try:
        if fmtTokenized == "str":
            print(f"{msgB.decode()}\nde\n{addr}\n\n")
        elif fmtTokenized == "pack":
            print(f"{unpack(msgB.decode())}\nde\n{addr}\n\n")
        elif fmtTokenized == "json":
            # Can work with binairies, but we will stick with ascii strings
            print(f"{json.loads(msgB.decode())}\nde\n{addr}\n\n")
        else:
            #We have already checked before that the format is ok
            print(f"{pickle.loads(msgB)}\nde\n{addr}\n\n")
            # Pcikle works with binary data
    except:
        print(addr, " a envoyé n'importe quoi", "\n\n")