import re

'''
O * quer dizer que corresponda a zero ou mais.
'''

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())