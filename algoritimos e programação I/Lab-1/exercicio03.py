'''
CONTA DE ENERGIA

Escreva um programa que determine o valor total a ser pago pela conta de energia elétrica, com base nas seguintes entradas:

O consumo de energia (em kWh); e
O tipo de instalação (R para residências, I para indústrias, e C para comércios).
Como saída :

1. Valor total da conta de energia elétrica arrendodado para duas casas decimais,
caso os dados sejam válidos OU a mensagem "Dados invalidos" caso os  dados sejam invalidos.
Os dados sao inválidos quando o consumo é negativo ou tipo de instalação diferente das letras R, I ou C.

O valor da conta depende do consumo e do tipo de local. Use a tabela a seguir para calcular o valor devido:


Preço por tipo e faixa de consumo
Tipo			Consumo (em kWh)	Preço (por kWh)
Residencial		Até 500				R$ 0,44
				Acima de 500		R$ 0,65
Comercial		Até 1000			R$ 0,55
				Acima de 1000		R$ 0,60
Industrial		Até 5000			R$ 0,55
				Acima de 5000		R$ 0,60
Validação dos dados:
Se o usuário inserir valores de entrada inválidos, imprima:

Entradas: X kWh e tipo Y

Dados invalidos

Se as entradas forem válidas, imprima:

Entradas: X kWh e tipo Y

Valor total: R$ Z

Nas mensagens de saída, substitua as letras X, Y e Z pelos valores correspondentes.
'''


consumo = float(input())
tipo = input().upper()
if consumo > 0 and tipo in "RCI":	
	if tipo == 'R':
		if consumo <= 500:
			valor = consumo * 0.44
		else:
			valor = consumo * 0.65
		print("Entradas: {} kWh e tipo {}".format(consumo,tipo))
		print("Valor total: R$ {}".format(round(valor,2)))
	elif tipo == 'C':
		if consumo <= 1000:
			valor = consumo * 0.55
		else:
			valor = consumo * 0.60
		print("Entradas: {} kWh e tipo {}".format(consumo,tipo))
		print("Valor tottal: R$ {}".format(round(valor,2)))
	elif tipo == 'I':
		if consumo <= 5000:
			valor = consumo * 0.55
		else:
			valor = consumo * 0.60
		print("Entradas: {} kWh e tipo {}".format(consumo,tipo))
		print("Valor total: R$ {}".format(round(valor,2)))
else:
		print("Entradas: {} kWh e tipo {}".format(consumo,tipo))
		print("Dados invalidos")
