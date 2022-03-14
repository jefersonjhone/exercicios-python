'''
DOIS INTERVALOS DE VALORES
Considere dois intervalos numéricos sobre a reta real: 
[a, b] e [c, d].
Escreva um programa que verifique se existe interseção (pelo menos um ponto em comum) entre os intervalos.

Se houver interseção, o programa deverá imprimir:
Intervalo 1: a , b

Intervalo 2: c , d

Ha intersecao

Se não houver interseção, o programa deverá imprimir:
Intervalo 1: a , b

Intervalo 2: c , d

Nao ha intersecao

Por fim, se as entradas forem inválidas, o programa deverá imprimir:
Intervalo 1: a , b

Intervalo 2: c , d

Entradas invalidas

Nas mensagens, substitua as letras a, b, c, d pelos valores fornecidos como entrada.
'''


a = float(input())
b = float(input())
c = float(input())
d = float(input())
if b > a and d > c:
    if b >= c and d >= a:
        print('Intervalo 1: {} , {}'.format(a, b))
        print('Intervalo 2: {} , {}'.format(c, d))
        print('Ha intersecao')
    elif b < c or d < a:
        print('Intervalo 1: {} , {}'.format(a, b))
        print('Intervalo 2: {} , {}'.format(c, d))
        print('Nao ha intersecao')
else:
    print('Intervalo 1: {} , {}'.format(a, b))
    print('Intervalo 2: {} , {}'.format(c, d))
    print('Entradas invalidas')
