#CONDICIONAL SIMPLES(IF)
nota1 = 6.00
nota2 = 7.00
media = (nota1 + nota2) / 2

'''
if media >= 7.00: #condicional 
    print('O aluno foi aprovado!\n') #comando a ser executado caso a condicional seja verdadeira
    print('Parabéns!')

print('A média é %f ' % media)
'''

#CONDICIONAL COMPOSTA
'''
O resultado de um teste sempre será binario (verdadeiro ou falso)
portanto apenas um bloco de instruções pode ser executado 
'''
'''
if media >= 7.00: #condicional 
    print('O aluno foi aprovado!\n') #comando a ser executado caso a condicional seja verdadeira
    print('Parabéns!')
else: #caso o retorno da condicional seja falso
    print('O aluno foi reprovado')
    print('Estude mais!!!!')

print('A média é %f ' % media)
'''
#CONDICIONAL ANINHADA
if media >= 7.00: #condicional 
    print('O aluno foi aprovado!\n') #comando a ser executado caso a condicional seja verdadeira
    print('Parabéns!')
elif media >= 5.00: #caso o retorno da condicional seja falso
    print('Aluno em recuperação')
else: #caso condicional2 seja falso
    print('O aluno foi reprovado')
    print('Estude mais!!!!')

print('A média é %f ' % media)
