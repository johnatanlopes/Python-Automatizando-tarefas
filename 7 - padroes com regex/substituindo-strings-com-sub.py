import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.'))