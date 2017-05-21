class PessoaCorreio():
	def __init__(self,cep,num,pedido,Domicilio='casa'):
		self.cep = cep
		self.num = num
		self.pedido = pedido
		self.Domicilio = Domicilio
	def MostrarPedido(self):
		print(self.pedido)
	def EntregaPedido(self):
		print("Pedido está sendo entregue paraa rua de cep: ",self.cep,\
			"numero: ",self.num)

class PessoaBoletim():
	def __init__(self,frequencia,ano,*notas):
		self.ano =ano
		self.notas = notas
		self.frequencia = frequencia
	def Verifica(self):
		if sum(self.notas)/len(self.notas) >= 6:
			if self.frequencia >= 0.75*200:
				print("passou")
			else:
				print("Faltou em muitas aulas.Irá repetir")
		else:
			print("media não foi alcançada.")
class PessoaRegCivil():
	def __init__(self,**kargs):
		self.sis = kargs
	def MostraDados(self):
		for d in self.sis:
			print(d,": ",self.sis[d])
	def MostraDadoEspc(self,dado):
		print(dado,": ",self.sis[dado])

REG = PessoaRegCivil(cpf=12345678,rg=123456,Nasc="12/3/2000",\
	Nome="Caio Henrique Vital Wanderley",Nacionalidade="Maceió - AL(Brazil)")
BOL=PessoaBoletim(190,2,4,6,10,9)
Correio=PessoaCorreio(57035665,67,"iphone")
Correio.MostrarPedido()
Correio.EntregaPedido()
BOL.Verifica()
REG.MostraDados()
REG.MostraDadoEspc("cpf")
