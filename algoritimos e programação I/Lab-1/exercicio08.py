'''
QUAL O MÊS?
Escreva um programa que leia um valor inteiro m 
tal que 1 ≤ m ≤ 12.

Como saída, imprima por extenso o nome do mês correspondente no ano.

Se a entrada não corresponder a nenhum dos meses do ano, imprima: numero de mes invalido
'''



#com lista este exercicio teria 5 linhas
numero = int(input())
if 1 <= numero <= 12:
    if numero == 1:
        print('janeiro')
    if numero == 2:
        print('fevereiro')
    if numero == 3:
        print('março')
    if numero == 4:
        print('abril')
    if numero == 5:
        print('maio')
    if numero == 6:
        print('junho')
    if numero == 7:
        print('julho')
    if numero == 8:
        print('agosto')
    if numero == 9:
        print('setembro')
    if numero == 10:
        print('outubro')
    if numero == 11:
        print('novembro')
    if numero == 12:
        print('dezembro')
else:
    print('numero de mes invalido')