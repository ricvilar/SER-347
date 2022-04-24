#Entrada do nome do arquivo
nome_sat = input('Entre com os dados do Satélite no formato correto USGS: ')

#Listas
a = nome_sat.split('.')
b = (a[1])
c = (a[2])
d = (a[4])

#Condicional
if 'MOD' not in a[0]:
    print('Nome não está correto, tente novamente')
    nome_sat = input('Entre com os dados do Satélite no formato correto USGS: ')
else:
    'MOD' in a[0]
    sat = 'Terra'
    print('Satellite...............: {}'.format(sat))
    print('Product.................: {}'.format(a[0]),
        '\nYear of Acquisition.....: {}'.format(b[1:5]),
        '\nJulian Day..............: {}'.format(b[5:8]),
        '\nHorizontal Tile.........: {}'.format(c[1:3]),
        '\nVertical Tile...........: {}'.format(c[4:6]),
        '\nCollection..............: {}'.format(a[3]),
        '\nYear of Production......: {}'.format(d[0:4]),
        '\nJulian Day of Production: {}'.format(d[4:7]),
        '\nProduction Hour.........: {}'.format(d[7:9]),
        '\nProduction Minute.......: {}'.format(d[9:11]),
        '\nProduction Second.......: {}'.format(d[11:13]),
        '\nData Format.............: {}'.format(a[5]),
          )



