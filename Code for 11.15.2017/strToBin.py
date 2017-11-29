s = ''
testString = 'Seacoast School of Technology Computer Science Program'
for ch in testString:
    s += '{0:08b}'.format(ord(ch))
print(s)
