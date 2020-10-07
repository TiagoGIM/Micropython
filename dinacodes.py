#set router mode in your server
"""
Este codigo foi feito para ajudar @dinalivia em um de seus projetos de graduação.
"""

import network
ap_if = network.WLAN(network.AP_IF)
#configurando o nodeMCU no modo acess point
ap_if.config(essid="dinalivia", authmode=network.AUTH_WPA_WPA2_PSK, password="dinalivia")

# set the simple server

import socket
HOST = ''              
PORT = 5000            
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print ("Ready",udp)
while True:
    msg, cliente = udp.recvfrom(1024)
    print (cliente, msg)
udp.close()


# set station mode and static ip in  your client
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.ifconfig(('192.168.4.5','255.255.255.0','192.168.1.1','192.168.0.1'))
sta_if.connect('dinalivia','dinalivia')

# set the simple client udp 
from socket import *
host = "192.168.4.1"  
port = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
addr =( host, port)
msg = "My string"
clientSocket.sendto(msg, addr)
