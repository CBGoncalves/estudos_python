import math #importa o modulo math com funcoes matematicas

print(math.pi) #retorna o valor de pi

print(math.sqrt(81)) #retorna a raiz quadrada de 81
b = 10
print(math.sqrt(b)) #retorna a raiz quadrada da variável b como parametro

c = -5
print(math.fabs(c)) #retorna o valor absoluto usando como parametro a variavel c

print(math.factorial(6)) #retorna o fatorial de 6
d = math.factorial(7) #declara a variavel d como fatorial de 7
print (d) #retorna a variavel d imprimindo o fatorial de 7

print(math.log10(8)) #retorna o logaritmo na base 10 do parametro 8
c = math.log10(15) #declara a variavel c como logaritmo de base 10 do numero 15
print (c) #retorna a variavel c imprimindo o logaritmo de 15

print(math.pow(5,3)) #retorna o resultado de 5 elevado a potencia 3
e = math.pow(6,2) #declara a variavel e como o valor da exponenciacao de 5 elevado a 2
print(e) #retorna a variavel c imprimindo a exponenciacao de 6 elevado a 2(retorna float)
print (6 ** 2) #o mesmo resultado pode ser obtido por meio do operador numerico de exponenciacao (retorna int)

c = 8/5 #declara c como a divisao entre 8 e 5
print(c) #imprime o resultado da divisao (1.6)
print(math.ceil(c)) #retorna o menor inteiro maior ou igual a x(arredonda para cima)
print(math.floor(c)) #retorna o maior inteiro menor ou igual a x(arredonda para baixo)

#Teste : Qual o valor retornado pela seguinte expressao?
#math.log10(math.sqrt(math.pow(2,7)-2**2*7))
c = math.log10(math.sqrt(math.pow(2,7)-2**2*7))
print(c)
#2**2= 4*7= 28
#math.pow(2,7)= 2**7= 128-28= 100
#math.sqrt(128)= 10
#math.log10(10)= 1.0
