import pyperclip

# Recebe o código da área de transferência
text = pyperclip.paste()

# Quebrar o texto e adicionar o * na frente
lines = text.split('\n')
for i in range(len(lines)): 
    lines[i] = ' * ' + lines[i]

# Juntar as linhas modificadas
text = '\n'.join(lines)

# Copiar para a área de transferência
pyperclip.copy(text)


