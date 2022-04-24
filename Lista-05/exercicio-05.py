import unidecode


def frasepalindromo(a):
    a = a.lower()
    a = ''.join(i for i in a if i.isalnum())
    a = a.replace('', '')
    a = unidecode.unidecode(a)
    return a == a[::-1]


chr = input('Digite a frase: ')
ver = frasepalindromo(chr)

if ver:
    print('A frase', chr, 'é um palindromo')
else:
    print('A frase', chr, 'não é um palindromo')