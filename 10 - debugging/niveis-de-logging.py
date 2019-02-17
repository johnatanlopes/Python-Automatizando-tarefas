'''
Os níveis de logging oferecem uma maneira de classificar suas mensagens de log de acordo com a importância. Há cinco níveis de logging:

    DEBUG - logging.debug() - É o nível mais baixo. Usado para pequenos detalhes. Geralmente você estará interessado nessas mensagens somente quando estiver
        diagnosticando problemas

    INFO - logging.info() - Usado para registrar informações sobre eventos em geral em seu programa ou para confirmar se tudo está funcionando nesse ponto do programa

    WARNING - logging.warning() - Usado para indicar um problema em potencial que não impede o programa de funcionar, porém poderá fazer isso no futuro

    ERROR - logging.error() - Usado para registrar um erro que fez o programa falhar em fazer algo

    CRITICAL - logging.critical() - É o nível mais alto. Usado para indicar um erro fatal que fez ou está prestes a fazer o programa parar totalmente de executar

Sua mensagem de logging será passada como uma string a essas funções; 
'''

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has ocurred.')
logging.critical('The program is unable to recover!')

'''
A vantagem dos níveis de logging está no fato de você poder alterar a prioridade da mensagem de loggin que você quer ver. Passar logging.DEBUG para o argumento
nomeado level da função basicConfig() mostrará as mensagens de todos os níveis de logging(DEBUG é o nível mais baixo). Entretanto, após desenvolver um pouco mais o 
seu programa, talvez você interesse somente pelos erros. Nesse caso, o argumento level de basicConfig() poderá ser definido para logging.ERROR. Isso fará somente as
mensagens ERROR e CRITICAL serem mostradas, enquanto as mensagens DEBUG, INFO e WARNING serão ignoradas
'''

# Desabilitando o logging
'''
Após ter feito o debugging de seu programa, talvez você não queira todas essas mensagens de log enchendo a tela. A função logging.disable() as desabilita
de modo que não seja necessário alterar o seu programa e remover todas as chamadas de logging manualmente. Basta passar um nível de logging a logging.disable()
e todas as mensagens de log desse nível ou abaixo dele serão suprimidas. Sendo assim, se você quiser desabilitar totalmente o logging, basta adicionar
logging.disable(logging.CRITITAL) ao seu programa.
'''

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.critical('Cirital error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error!')
logging.error('Error')
