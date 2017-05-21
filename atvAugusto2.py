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
		if VerbaUsar > self.Verba:
			print("Verba EXtrapolada")
		else:
			self.Verba-=VerbaUsar
class Ecossistema():
	def __init__(self,Fator,Tipo=''):
		if Fator.lower() == 'biótico':
			Tipo = input('1 - Produtor,2 - Consumidor ou 3 - Decompositor?')
		self.Fator = Fator
		self.Tipo = Tipo
		self.Chovendo = False
	def chover(self):
		self.Chovendo = True
	def PararChover(self):
		self.chovendo = False
class SistemaDeEstacionamento():
	def __init__(self,Vagas,VagasDefi=1,VagaIdoso=1):
		self.Vagas=Vagas
	def estaciona(self):
		if self.Vagas !=0:
			self.Vagas-=1
		else:
			print("Não tem vagas")
class SistemaAereo():
	def __init__(self,**kargs):
		self.Voos = {}
		for x,d in enumerate(kargs):
			self.Voos[x] = [d,kargs[d],'espera']
		self.Nums = x	
	def MostraVoo(self,numero):
		for d in self.Voos.items():
			print("numero: ",d[0],"Destino: ",d[1][0],"Horario: ",d[1][1],"Estado: ",d[1][2])
	def Decolar(self,num):
		self.Voos[num].pop(2)
		self.Voos[num].append('Decolado')
	def Cancelar(self,num):
		self.Voos[num].pop(2)
		self.Voos[num].append('Cancelado')
	def Chegada(self,num):
		self.Voos[num].pop(2)
		self.Voos[num].append('Chegou')
