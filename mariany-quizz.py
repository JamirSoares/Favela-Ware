# by Mateus e Evandro

from ast import While
from random import randint
from pyfiglet import figlet_format
print(figlet_format('nao sei'))

listaPerguntas = [
    'o que é usado para a entrada de dados no python?',

    'o que é usado para a saída de dados em python?',

    'qual tipo de variável é usada para indicar um valor inteiro?',

    'qual tipo de variável é usada para indicar números decimais e é também conhecido como ponto flutuante?',

    'qual tipo de variável indica um texto?',

    'quais valores o tipo de variável bool indica?'
]


listaRespostas = [[
    'a.input\n',
    'b.inteiro'],

    ['a.input\n',
     'b.print'],

    ['a.str\n',
     'b.int'],

    ['a.float\n',
     'b.boolean'],

    ['a.string\n',
     'b.input'],

    ['a.grande e pequeno\n',
     'b.verdadeiro e falso']]

gabarito = ['a',
            'b',
            'b',
            'a',
            'a',
            'b']
respostasCertas = 0
respostasErradas = 0
aleatorio = randint(0, 5)
print('responda as questões a seguir sobre python')

for indice in range(len(listaPerguntas)):
    aleatorio = randint(0, 5)
    print(str(listaPerguntas[aleatorio]))

    for i in range(len(listaRespostas[aleatorio])):
        print('\n'+listaRespostas[aleatorio][i])
    resposta = input('>>')
    if(resposta == gabarito[aleatorio]):
        respostasCertas = respostasCertas + 1
        print('Acertou mizeravi')
    if(resposta != gabarito[aleatorio]):
        respostasErradas = respostasErradas + 1
        print('se fudeo')

print('acertos: ' + str(respostasCertas))
print('erros: ' + str(respostasErradas))
input()
