'''
Se a chamada a smtplib.SMTP() não for bem sucedida, é sinal de que seu servidor SMTP talvez não suporte TLS na porta 587. Nesse caso, será necessário criar um
objeto SMTP usando smtplib.SMTP_SSL('smtp.gmail.com', 465).

Depois que você tiver o objeto SMTP, chame seu método ehlo(), de nome inusitado, para dizer 'Alo' apo seu servidor de emails SMTP. Essa saudação é o primeiro passo no
SMTP e é importante para estabelecer uma conexão com o servidor. Não é preciso conhecer os detalhes desse protocolo. Basta garantir que o método ehlo() seja inicialmente
chamado após obter o objeto SMTP; do contrário, as chamadas de métodos feitas posteriormente resultarão em erros. Se o primeiro item da tupla retornada for o inteiro 250
que é o codigo para sucecsso no SMTP é sinal de que a saudação foi bem sucedida.

Depois que sua conexão criptografada com o servidor SMTP estiver configurada, você poderá fazer login com seu nome de usuário e senha.
O valor de retorno 235 indica que a autenticação foi bem sucedida. O python retornará uma excelçao smtplib.SMTPAuthenticationError para senhas incorretas.

Após ter feito login no servidor SMTP, o método sendmail() poderá ser chamado para enviar o email.

O método sendmail() exige três argumentos:
    - Seu endereço de email como uma string. Para o endereço from.
    - O endereço de email do destinarário como uma string ou uma lista de strings para vários destinatários. Para o endereço to
    - O corpo do email como uma string.
        O início da string com o corpo do email deve começar com 'Subject: \n' para a linhad e assunto do email. O caractere '\n' quebra de linha separa o assunto
        do corpo do email principal. 

O valor de retorno de sendmail() é um dicionário. Haverá um par de chave-valor no dicionário para cada destinatário a quem a entrega do email falhar. Um dicionário
vazio indica que o email foi enviado com sucesso a todos os destinatários.

O valor de retorno 221 indica que a sessão foi encerrada.
'''

import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtpObj.ehlo())
print(smtpObj.starttls())
print(smtpObj.login('seuemail@gmail.com', 'suasenha'))

try:
    smtpObj.sendmail('seuemail@gmail.com', 'destinarario@gmail.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
    smtpObj.quit()
except Exception as e:
    print(e)


