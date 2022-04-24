entrada = 'Gilberto'
saida = '{:+^12}'.format(entrada)
print(saida)

entrada = 'sensoriamento remoto'
saida = entrada.capitalize()
print(saida)

entrada = 'sensoriamento remoto'
saida = entrada.title()
print(saida)

entrada = 'GilberTo'
saida = entrada.lower()
print(saida)

entrada = 'Gilberto'
saida = '{:*<10}'.format(entrada)
print(saida)

entrada = 'Gilberto'
saida = '{:*>10}'.format(entrada)
print(saida)

entrada = ' Gilberto'
saida = entrada.strip()
print(saida)

entrada = 'ser347@dpi.inpe.br'
saida = entrada.partition('@')
print(saida)

entrada = 'CBERS_4_PAN5M_20180308'
saida = entrada.split('_')
print(saida)

entrada = 'Gilberto@@@'
saida = entrada.strip('@')
print(saida)

entrada = '@@Gilberto@@@'
saida = entrada.strip('@')
print = saida
