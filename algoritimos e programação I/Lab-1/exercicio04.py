'''
INTERVALO DE VALORES
Considere dois números reais a e b, sendo b > a. Um número real 
x pertence ao intervalo [ a, b] se a ≤ x ≤ b.

Escreva um programa que leia os números reais x, a, b, nesta ordem.

Se x pertencer ao intervalo, imprima a seguinte mensagem:
x pertence ao intervalo a , b

Caso contrário, imprima a seguinte mensagem:
x nao pertence ao intervalo a , b

Se as entradas forem inválidas, ou seja, se b ≤ a, imprima a seguinte mensagem:
Entradas a e b invalidas

Nas mensagens, substitua as letras x, a, b pelos valores fornecidos como entrada.
'''


x = float(input())
a = float(input())
b = float(input())
if a< b:
    if a <= x and x <= b:
        print('{} pertence ao intervalo {} , {}'.format(x,a,b))
    else:
        print('{} nao pertence ao intervalo {} , {}'.format(x,a,b))
else:
    print('Entradas {} e {} invalidas'.format(a,b))