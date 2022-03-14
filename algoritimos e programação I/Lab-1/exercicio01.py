'''QUAL O TIPO DE TRIÂNGULO?

Escreva um programa que leia três números reais, correspondentes às medidas dos lados de um triângulo, em ordem qualquer.

Dados de entrada:

1. Lado A

2. Lado B

3. Lado C

Como saída, o programa deverá imprimir:

Entradas: A, B, C

Tipo de triangulo: X

No comando print() as letras  A, B, C devem ser substituídas pelos valores de entrada informados pelo usuário.
Substitua a letra X por um dos seguintes valores:
equilatero, se todos os três lados forem iguais;
isosceles, se apenas dois lados forem iguais;
escaleno, se nenhum par de lados forem iguais;
invalido, se pelo menos um dos lados for negativo ou se os três lados não formarem um triângulo.
'''


lado_a = float(input())
lado_b = float(input())
lado_c = float(input())
if lado_a > 0 and lado_b > 0 and lado_c > 0:
	if lado_a +lado_b >lado_c and lado_a +lado_c >lado_b and lado_b + lado_c > lado_a:
		if lado_a == lado_b == lado_c:
			print("Entradas: {} , {} , {}".format(lado_a,lado_b,lado_c))
			print('Tipo de triangulo: equilatero')
		elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
			print("Entradas: {} , {} , {}".format(lado_a,lado_b,lado_c))
			print("Tipo de triangulo: isosceles")
		else:
			print("Entradas: {} , {} , {}".format(lado_a,lado_b,lado_c))
			print('Tipo de triangulo: escaleno')
	else :
		print("Entradas: {} , {} , {}".format(lado_a,lado_b,lado_c))
		print('Tipo de triangulo: invalido')
else :
	print("Entradas: {} , {} , {}".format(lado_a,lado_b,lado_c))
	print('Tipo de triangulo: invalido')