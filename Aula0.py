#print('olá mundo!')

"""
aluno = 'isadora'
print(type (aluno)) #- mostra qual é a classe - str(string)

aluno = 4
print(type(aluno))

aluno = 4/7
print(type(aluno))
"""

#LISTA
"""
lista = ['banana', 'uva', 'morango', 7, True, [1, 2, 3, ['carro', 'casa']]]
#lista.append('laranja') - add elemento

#print(lista[3]) - posição da lista

for fruta in lista:
    print(fruta)
    
"""

#dict (dicionário) - chave valor
"""
dicio = {}
dicio ['nome'] = 'isadora'
dicio['nota'] = 8
dicio['idade'] = 17

#print(dicio)

for dado in dicio:
    print(dado) #só pega o valor que está na chave

for chave, valor in dicio.items():
    print(chave, valor)
"""

#for i in range(7): inicio no 0
   # print(i)
   
#for i in range(2, 7): inicia no 2
    #print(i)

#for i in range(20, 7, -2): inicia no 20 e vai até o 7 pulando de 2 em 2
    #print(i)
    

# IF
"""
for i in range(30):
    if i%3==0:
        print('pim')
    else:
        print(i)


nota = 10

if nota > 9:
    print('A')
elif nota < 8:
    print('C')
else: 
    print('D')
"""

#FUNÇÃO - não tem uma classe definida (ex: str, int...)

def imprimir(nome):
    print('oi', nome)
    #print(f' {saudacao}, {nome} !!') - deixar formatado

    
imprimir('isadora')

def soma_multiplicacao(x, y):
    soma = x + y
    mult = x * y
    return soma, mult


def main():
    #retorno = soma_multiplicacao(3,9)
    s, m = soma_multiplicacao(3,9)
    print(s, m)
    
    #imprimir()
    #imprimir('isadora')
    #print('fim')
    
main()
