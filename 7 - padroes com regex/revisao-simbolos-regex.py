'''

?       -   Correspondee a zero ou uma ocorrência do grupo anterior.
*       -   Corresponde a zero ou mais ocorrências do grupo anterior.
+       -   Corresponde a uma ou mais ocorrências do grupo anterior.
{n}     -   Corresponde a exatamente n ocorrências do grupo anterior.
{n, }   -   Corresponde a n ou mais ocorrências do grupo anterior.
{, m}   -   Corresponde a zero até m ocorrências do grupo anterior.
{n, n}  -   Corresponde a no mínimo n e no máximo m ocorrências do grupo anterior.
{n, m}? ou *? ou +?   -   Faz uma correspondência nongreedy do grupo anterior.
^spam   -   A string deve começar com spam.
spam$   -   A string deve terminar com spam.
.       -   Corresponde a qualquer caractere, exceto os caractres de quebra de linha.
\d, \w e \s     -   Correspondem a um dígito, um caractere de palavra ou um caractere de espaço, respectivamente.
\D, \W e \S     -   Correspondem a qualquer caractere, exceto um dígito, um caractere de palavra ou um caractere de espaço, respectivamente.
[abc]   -   Corresponde a qualquer caractere que estiver entre os colchetes por exemplo a, b ou c.
[^abc]  -   Coprresponde a qualquer caractere que não esteja entre os colchetes.

'''