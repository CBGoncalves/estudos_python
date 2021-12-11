s = "pizza"
print(s)

l = "carlos,eduardo,pietro,marcelo,mateus,guilherme,henrique,pedro"

print(s.find("iz"))#encontra a posição de uma substring

print(s.replace("zza","não"))#substitui uma substring por outra não altera a string original

print(s.upper())#transforma os caracteres da string em maiusculos
print(s.lower())#converte os caracteres da string em minusculos

print(s.isalpha())#verifica se o conteudo da string e alfabetico, retorna boolean(true ou false)
print(s.isalnum())#verifica se o conteudo da string e alfanumerico, retorna boolean(true ou false)

print(s.lstrip("p"))#remove os caracteres a esquerda, caso nao tenha parametro remove espacos em branco
print(s.rstrip("p"))#remove os caracteres a direita

print(s.capitalize())#retorna a string com o primeiro caracter maiusculo

print(l.split(","))#retorna uma lista de itens delimitada pelo caracter especificado
