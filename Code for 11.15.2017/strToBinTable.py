uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lc = 'abcdefghijklmnopqrstuvwxyz'
space = ' '
symbols = '!@#$%^&*()_+-=<>/?\|[{]},.'
numbers = '0123456789'

for ch in lc:
    print(ch + '     ' + '{0:08b}'.format(ord(ch)))
print()
for ch in lc:
    print(ch + '     ' + '{0:08b}'.format(ord(ch)))
print()
for ch in symbols:
    print(ch + '     ' + '{0:08b}'.format(ord(ch)))
print()
for ch in numbers:
    print(ch + '     ' + '{0:08b}'.format(ord(ch)))
print()   
print('Space' + '     ' + '{0:08b}'.format(ord(' ')))
