class Transporte():

	def __init__(self,Tipo,vel):
		self.acelerar = vel
		self.velNow = 0
		self.position = 0
		self.Tipo = Tipo

	def Movimentar(self,time):
		position = self.acelerar * time
		self.position+= position
		self.velNow += self.acelerar/60

	def Freiar(self,qnt):
		self.velNow -= qnt

class Materiais():

	def __init__(self,material,Qnt = 10):
		self.material = material
		self.Quantidade = Qnt

	def Pregar(self,Usar):
		self.Quantidade -= Usar

class Abrigos():

	def __init__(self,Tipo,resistence):
		self.Tipo = Tipo
		self.resistence = resistence
		self.PortaAberta = False

	def Abrir(self):
		self.PortaAberta = True

	def Fechar(self):
		self.PortaAberta = False
