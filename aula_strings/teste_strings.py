a = "abacaxi"
print (a)

s = "minha string"
x = len(s) #x verifica o comprimento(length) da string s
print(x) #imprime o comprimento da string s(12)

print(s[0]) #acessa e imprime um caracter individual da string s de acordo com  o indice passado como parametro
print(s[1]) 
print(s[2])
print(s[3])
print(s[4])

print(s[2:6]) #imprime uma fatia(slicing) da cadeia de acordo com os indices passados como parametro(o ultimo tem um caracter subtraido)
print(s[1:]) #imprime do segundo ao ultimo caracter
print(s[-1]) #inverte a contagem imprimindo o ultimo caracter

print(s + " nova") #concatenacao junta duas ou mais strings formando uma nova

print(s * 6) #repete a string s 6 vezes
print((s + " ") * 6) #repete a string s 6 vezes porem concatenando um espaço entre as repeticoes

#s[0] = "b" #strings sao imutaveis se tentarmos acessar um indice e altera-lo isso causara um erro

#retorne os 3 primeiros caracteres da string "Linux"
l = "Linux"
print(l[0:3])


