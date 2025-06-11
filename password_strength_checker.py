'''
problem:check if password is 'weak', 'medium', or 'strong', criteria: < 6 chars (weak), 6-10 chars (medium), > 10 chars(strong)
'''



password = input('enter your password:')

if len(password) < 6:
    print('weak')
elif len(password) < 10:
    print('medium')
else:
    print('strong')