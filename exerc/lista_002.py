#Lista 2 - Estruturas de Decisão

'''
1.Faça um Programa que peça dois números e imprima o maior deles.
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número é o maior: %d' % num1)
elif num2 > num1:
    print('O segundo número é o maior: %d' % num2)
elif num1 == num2:
    print('Os dois números são iguais: %d' % num1)

'''
2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
num = int(input('Digite um número: '))

if num > 0:
    print('O número digitado é positivo(%d)' % num)
elif num < 0:
    print('O número digitado é negativo(%d)' % num)
elif num == 0:
    print('O número digitado é neutro(%d)' % num)

'''
3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = input('Digite seu sexo, F(Feminino) ou M(Masculino): ')
if sexo == 'F':
    print('Sexo feminino')
elif sexo == 'M':
    print('Sexo masculino')
else:
    print('Sexo inválido')

'''
4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input('Digite uma letra: ')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('A letra %s é uma vogal' % letra)
else:
    print('A letra %s é uma consoante' % letra)

'''
5.Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
-A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
-A mensagem "Reprovado", se a média for menor do que sete;
-A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 7:
    print('Reprovado')
elif media == 10.0:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')

'''
6.Faça um Programa que leia três números e mostre o maior deles.
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O primeiro número é o maior(%d)' % n1)
elif n2 > n1 and n2 > n3:
    print('O segundo número é o maior(%d)' % n2)
elif n3 > n2 and n3 > n1:
    print('O terceiro número é o maior(%d)' % n3)

'''
7.Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#achar o maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
#achar o menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3
#retorna o maior e o menor
print('O maior número é: %d' % maior)
print('O menor número é: %d' % menor)

'''
8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
print('-------Comparador de Preços-------')

produto1 = float(input('Informe o preço do primeiro produto: '))
produto2 = float(input('Informe o preço do segundo produto: '))
produto3 = float(input('Informe o preço do terceiro produto: '))

if produto1 < produto2 and produto1 < produto3:
    print('O primeiro produto deve ser comprado (preço: R$%f)' % produto1)
elif produto2 < produto1 and produto2 < produto3:
    print('O segundo produto deve ser comprado (preço: R$%f)' % produto2)
elif produto3 > produto2 and produto3 > produto1:
    print('O terceiro produto deve ser comprado (preço: R$%f)' % produto3)

'''
9.Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
