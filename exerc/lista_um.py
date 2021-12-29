#LISTA DE EXERCIOS

'''
1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.
'''
print('Alo Mundo')

'''
2. Faça um programa em linguagem Python que converta metros para centímetros.
'''
print('\t ----Conversão de medida----')
m = int(input('Informe o valor em metros: '))
print('O valor em centimetros é :', m * 100)

'''
3.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''
print('\t ----Mostre o numero----')
numero = int(input('Informe um numero: '))
print('O numero informado foi:', numero)

'''
4.Faça um Programa que peça dois números e imprima a soma.
'''
print('\t ----Soma de dois numeros----')
x = int(input('Informe o primeiro numero: '))
y = int(input('Informe o numero que deve ser somado a %d: ' % x))
print('A soma dos numeros {0} e {1} é:'.format(x,y), x + y)

'''
5.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
print('\t ----Média bimestral----')
print('Informe suas quatro notas:')
nota1 = float(input('1°: '))
nota2 = float(input('2°: '))
nota3 = float(input('3°: '))
nota4 = float(input('4°: '))
print('Sua média bimestral é:', (nota1+nota2+nota3+nota4) / 4)

'''
6.Faça um Programa que converta centimetros para decimetros.
'''
print('\t ----Conversão de medidas 2----')
cm = int(input('Informe o valor em centímetros: '))
print('O valor em decímetros é:', cm / 10)

'''
7.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
print('\t ----Área do Circulo----')
r = int(input('Informe o raio do círculo: '))
print('A área do circulo é', 3.14 * (r * r))

'''
8.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''
print('\t ----Dobro da área do quadrado----')
l = int(input('Informe a medida dos lados do quadrado: '))
print('A área deste quadrado é:', l * l)
print('O dobro desta área é:', (l * l) * 2)

'''
9.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
print('\t ----Salário Mensal----')
g = float(input('Informe quanto você ganha por hora: '))
h = int(input('Informe quantas horas você trabalhou no mês: '))
print('Neste mês você ganhou:', g * h)

'''
10.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''
print('\t ----Conversão de temperatura(°F - °C)----')
f = int(input('Informe a temperatura em graus Fahrenheit: '))
c = 5 * ((f - 32) / 9)
print('A temperatura de {0}°F é equicalente a {1}°C'.format(f,c))

'''
11.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
print('\t ----Conversão de temperatura(°C - °F)----')
c = int(input('Informe a temperatura em graus Celcius: '))
f = 32 + ((c * 9) / 5)
print('A temperatura de {0}°C é equicalente a {1}°F'.format(c,f))

'''
12.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo.
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
'''
import math
print('\t ----Informe dois números inteiros----')
i1 = int(input(': '))
i2 = int(input(': '))
print('\t ----Informe um número real----')
r = int(input(': '))
print('o produto do dobro do primeiro com metade do segundo é:', (i1 * 2) * (i2 / 2))
print('a soma do triplo do primeiro com o terceiro é:', (i1 * 3) + r)
print('o terceiro elevado ao cubo é:',math.pow(r,3))

'''
13.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''
print('\t ----Peso ideal----')
a = float(input('Informe sua altura(Ex:1.75): '))
print('Seu peso ideal de acordo com a sua altura é de:', (72.7 * a) - 58)

'''
14.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
print('\t ----Peso ideal 2----')
print('Informe seu sexo: Feminino(0) Masculino(1)')
s = int(input(': '))
h = float(input('Informe sua altura(Ex:1.75): '))
if s == 0:
    print('Sexo selecionado: Feminino')
    print('Seu peso ideal de acordo com a sua altura é:', (62.1 * h) - 44.7)
elif s == 1:
    print('Sexo selecionado: Masculino')
    print('Seu peso ideal de acordo com a sua altura é:', (72.7 * h) - 58)
elif s != 0 and s != 1:
    print('Informe um valor para sexo válido')

'''
15.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
'''
print('\t ----Peso do peixe----')
peso = float(input('Informe o peso do peixe em quilos(Ex:38): '))
excesso = peso - 50
multa = 4.00 * excesso
if peso > 50:
    print('excesso:', excesso)
    print('multa(R$):', multa)
else:
    print('O peixe não excede o peso')

'''
16.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
print('\t ----Rendimento Mensal----')
ganhoHora = float(input('Quanto você ganha por hora de trabalho(R$): '))
hora = int(input('Quantas horas você trabalhou no mês: '))
sb = ganhoHora * hora
print('Salário Bruto : R$', sb)
ir = sb * 0.11
print('IR (11%) : R$', ir)
inss = sb * 0.08
print('INSS (8%) : R$', inss)
sindicato = sb * 0.05
print('Sindicato (5%) : R$', sindicato)
sl = sb - ir - inss - sindicato
print('Salário Liquido : R$', sl)

'''
17.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
print('\t ----Loja de Tinta----')
coberturaLitro = 3
precoLata = 80.0
capacidadeLata = 18

metros = int(input("Digite a área em metros quadrados a serem pintados: "))
litros = metros / coberturaLitro

latas = int(litros / capacidadeLata)
if(litros%capacidadeLata != 0):
    latas += 1    
total = latas * precoLata

print('Quantidade de tinta(litros): ',litros)
print('Você usara ',latas,'latas de tinta')
print('O preco total é de: R$',total)

'''
18.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;
-misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
isto é, considere latas cheias.
'''
coberturaLitro = 6
capacidadeLata = 18
precoLata = 80.0

capacidadeGalao = 3.6
precoGalao = 25.0

metros = int(input("Digite a área em metros quadrados a serem pintados: "))
litros = metros / coberturaLitro

#comprar apenas latas
latas = int(litros / capacidadeLata)
if(litros%capacidadeLata != 0):
    latas += 1    
totalLatas = latas * precoLata

print('Quantidade de tinta(litros): ',litros)
print('Você usara ',latas,'latas de tinta')
print('O preco total é de: R$',totalLatas)

#comprar apenas galões
galoes = int(litros / capacidadeGalao)
if(litros%capacidadeGalao != 0):
    latas += 1    
totalGaloes = latas * precoLata

print('Quantidade de tinta(litros): ',litros)
print('Você usara ',galoes,'galoes de tinta')
print('O preco total é de: R$',totalGaloes)

#misturar latas e galões
if(litros%capacidadeLata != 0):
    galoes += 1    
total = (latas * precoLata) + (galoes * precoGalao)

print('Quantidade de tinta(litros): ',litros)
print('Você usara ',latas,'latas de tinta e ',galoes,'galões')
print('O preco total é de: R$',total)

'''
19.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
print('Tempo de download')
tamanho = int(input('Informe o tamanho do arquivo(Mb): '))
velocidade = int(input('Informe a velocidade da internet(Mbps): '))
tempo = tamanho / velocidade / 60
print('O tempo de aproximado de download do arquivo é de: ',tempo,' minutos')

