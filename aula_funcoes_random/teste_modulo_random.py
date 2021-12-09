import random #importa o modulo random e suas funcoes
import math

print(random.random()) #funcao que gera um numero aleatorio entre 0 e 1
print(10 * random.random()) #gera um numero aleatorio entre 1 e 10

print(math.floor(10 * random.random())) #arredonda os resultados da funcao random gerando apenas numeros inteiros

print(random.choice([2,4,6,8,10,12])) #escolhe um dos numeros da lista de forma aleatoria

print(random.choice(["laranja","banana","mamão","abacate"])) #escolhe uma das frutas da lista de forma aleatoria
