def palindromo(a):
    a = a.lower()
    return a == a[::-1]


chr=input('Digite a palavra: ')
ver = palindromo(chr)

if ver :
    print('A palavra {} é um Palindromo!'.format(chr))
else :
    print('A palavra {} não é um Palindromo!'.format(chr))
