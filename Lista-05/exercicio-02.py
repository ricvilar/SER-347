
fraco = True
while fraco:
    senha = input('Digite a senha: ')
    if len(senha) < 8 or not any(i.isupper() for i in senha) or not any(i.isupper() for i in senha):
        print('Senha fraca, por favor, digite uma nova senha!')
    else:
        print('Senha Forte')
        fraco = False