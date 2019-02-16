import re

'''
As vezes, há um padrão ao qual você quer corresponder somente de forma opcional.
Isso quer dizer que a regex deve encontrar uma correspondência independentemente de essa porção de texto estar ou 
não presente.
'''

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

batRegex = re.compile(r'Bat(wo)?man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phoneRegex.search('My number is 415-555-4242')
print(mo3.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('My number is 555-4242')
print(mo4.group())