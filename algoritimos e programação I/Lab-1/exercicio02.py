'''
De volta à área do triângulo

Escreva um programa para calcular a área de um triângulo,
a partir das medidas dos três lados,
fornecidas pelo usuário, em qualquer ordem.

O algoritmo não pode permitir a entrada de dados inválidos, ou seja,
medidas menores ou iguais a zero,
ou medidas que não correspondam às de um triângulo.
'''


a = float(input())
b = float(input())
c = float(input())
if a > 0 and b > 0 and c > 0:
	if a + b > c and a + c > b and b + c > a:
		#formula de heron		
		p = (a + b + c)/2
		area = (p*(p-a)*(p-b)*(p-c))**(1/2)
		print(round(area,1))
	else :
		print('Tipo de triangulo: invalido')