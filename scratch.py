
import usocket as socket
from machine import Pins

class iotreta:
	self.s = None

	def __init__(self ,config):
		self.config =  config		
		

	def connect(self):
		addr = socket.getaddrinfo(self.config['host'], self.config['port'])[0][-1]
		self.s = socket.socket()
		self.s.connect(addr)


	def send_thing(self , s, data, tipo = 'date'):

		data = {tipo:{
						'auth_thing':s[0],
						'auth,user':s[1],
						'date':data
						}
				}

		s.send(data)
		return s.recv(2014)



	def grafico(self ,s , value):

		data = {'x': value }

		status = self.s.send_thing(s,data,tipo = 'grafico')

		return status

	def input(self,pin):

		data = {'pin': pin }

		self.send_thing(self.s ,data ,tipo ='input')

		server_recive = self.s.recv(1024)

		status_pin_input = server_recive['pin'][pin]

		self.pinMode(pin , status_pin_input)

		return status_pin_input

	def output(self,pin):
		
		self.pin(pin)

		data = {'status': status_pin_output , 'pin': pin }

		self.send_thing(s,data,tipo ='output')

		server_recive = s.recv(1024)

		status_porta = server_recive['portas'][porta] 

	self.connect()

io = iotreta(config)

while True:
	if(io.input(13)):
		io.output(10)
		io.grafico(x)



