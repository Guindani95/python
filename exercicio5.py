# Exercicio 005
# Faça um Programa que converta metros para centímetros.
metros = float( input ('Insira a metragem:'))
valor = metros * 100
valor = f'{valor:_.2f} Centimetros'
valor = valor.replace('.',',').replace ('_','.')  #vi na internet sobre alterar para um modo que usamos no dia a dia , deu +- certo
print (f'Metragem em cm:{valor}')
