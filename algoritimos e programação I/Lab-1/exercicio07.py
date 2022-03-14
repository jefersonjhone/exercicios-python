'''
Índice de massa corporal (IMC)

Faça um programa que informe o risco de problemas cardíacos de uma pessoa, 
a partir da leitura da idade e do índice de massa corporal (IMC), nessa ordem.
Os riscos são definidos de acordo com a tabela a seguir:

 
IDADE       IMC         RISCO

< 45        < 22.0      Baixo
< 45        >= 22.0     Medio
≥ 45        < 22.0      Medio
≥ 45        >=22.0      Alto

 

Validação dos dados:

Verifique se os dados informados são válidos.
Se a idade for menor ou igual a zero ou maior que 130 anos,
ou se o IMC for menor ou igual a zero, imprima a seguinte mensagem:

Entradas: X anos e IMC Y
Dados invalidos

Se as entradas forem válidas, imprimir a seguinte mensagem:

Entradas: X anos e IMC Y

Risco: Z

Nas mensagens, substitua as letras X, Y e Z pelos valores correspondentes.
'''


idade = int(input())
imc = float(input())
if 0 < idade <=130 and imc > 0:
    if idade < 45 and imc < 22.0:
        print('Entradas: {} anos e IMC {}'.format(idade, imc))
        print('Risco: Baixo')
    elif idade < 45 and imc >= 22.0:
        print('Entradas: {} anos e IMC {}'.format(idade, imc))
        print('Risco: Medio')
    elif idade >= 45 and imc < 22.0:
        print('Entradas: {} anos e IMC {}'.format(idade, imc))
        print('Risco: Baixo')
    elif idade >= 45 and imc > 22.0:
        print('Entradas: {} anos e IMC {}'.format(idade, imc))
        print('Risco: Media')
else:
    print('Entradas: {} anos e IMC {}'.format(idade, imc))
    print('Dados invalidos')