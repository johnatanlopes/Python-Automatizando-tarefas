# pip3 install pyperclip

import sys, pyperclip

PASSWORDS = {'email': 'F7minLBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '123456'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # o primeiro argumento da linha de comando é o nome da conta

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS['account'])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('The is no account named ' + account)