#LISTAS

l = [] #lista vazia
L = [0, 1, 2, 3, 4] #lista de números
print(L)

'''
Métodos suportados por listas
'''
'''
Concatenação(+)
junção de litas
'''
L2 = [5, 6, 7, 8]
print(L + L2)

'''
Repetição(*)
multiplica o conteúdo da lista
imprimindo x vezes de acordo com o numero
multiplicado
'''
print(L2 * 5)

'''
Verificar se um valor exite na lista(in)
busca o valor na lista e retorna true, caso exista
ou false caso não exista
'''
print(4 in L)#True
print(1 in L2)#False

'''
Iteração(for)
substitui o valor definido por cada item da lista,
permitindo manipular varios itens de uma só vez
'''
L3 = ['Carlos', 'Eduardo', 'Pedro', 'Marcelo']
for x in L3: 
    print('Olá ' + x + ', com vai')

'''
Acrescentar Itens(append)
adiciona o item do parâmetro na lista
'''
L.append(9)#adiciona o item '9' na lista L
print(L)

'''
Inserir Item em uma Posição Específica(insert)
'''
L.insert(3, 12)#insere na posição 3 o valor 12
print(L)

'''
Buscar posição do item na lista(index)
'''
print(L.index(12))#posião 3
print(L.index(9))#posição 6

'''
Contar a ocorrência de um item na lista(count)
'''
L.append(2)#adiciona o valor 2 novamente a lista L
print(L.count(2))#ocorre 2 vez
