class SalaDeAula():
	def __init__(self,cadeiras,Computadores,arCondicionado):
		self.cadeiras = cadeiras
		self.Computadores = Computadores
		self.arCondicionado = arCondicionado
		self.excedente = 0

	def Entrar(self,QntPessoas):
		if QntPessoas > self.cadeiras:
			print("Deverá pegar mais cadeiras.")
		if QntPessoas > self.Computadores:
			print("Falta computadores,se juntem.")
		else:
			self.cadeiras -= QntPessoas
			self.Computadores -= QntPessoas

	def Sair(self,QntPessoas):
		if not self.excedente:
			self.Computadores -= QntPessoas
		self.cadeiras -= QntPessoas

class TransportesUrbanos():

	def __init__(self,Tipo,Disponiveis,VerbaMes,Gasolina):
		self.Tipo = Tipo
		self.Verba = VerbaMes
		self.Disponiveis = Disponiveis
		self.Gasolina = Gasolina

	def Manutencao(self,VerbaUsar):
		if VerbaUsar > self.Verba:
			print("Verba extrapolada.")

		else:
			self.Verba -= VerbaUsar
	def Abastecer(self,VerbaUsar):