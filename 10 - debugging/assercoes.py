'''
Uma asserção (assertion) é uma verificação de sanidade para garantir que seu código não está fazendo nada obviamente incorreto. Essas verificações de sanidade
são realizadas por instruções assert. Se a verificação de sanidade falha, uma exceção AssertionError será gerada. No código uma instrução assert é constituida das
seguintes partes:

    - a palavra-chave assert
    - uma condição (ou seja, uma expressão avaliada como True ou False)
    - uma vírgula
    - Uma string a ser exibida quando a condição for False

Falando de forma simples, uma isntrução assert diz: "Afirmo que esta condição é verdadeira, mas, se não for, há um bug em algum lugar do programa"
De modo diferente das exceções, seu código não deverá tratar as instruções assert com try e except; Se um asser falhar seu programa deve falhar. Ao falhar 
rapidamente dessa maneira, você reduzirá o tempo entre a causa original do bug e o momento em que ele será percebido pela primeira vez.

As asserções servem para identificar erros aos programadores, e não aos usuários. Os erros dos quais pode haver uma recuperação (por exemplo, um arquivo não encontrado)
ou a inserção de dados inválidos pelo usuário) devem gerar uma exceção de vez de serem detectados por uma instrução assert.
'''

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'closed'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
