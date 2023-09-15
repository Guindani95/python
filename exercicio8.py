# Exercicio 008
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

import datetime

salario = float ( input("Digite seu sálario:"))
horas_trabalhadas = int ( input("Horas trabalhadas mensais:"))
resultado = horas_trabalhadas * salario
print (f'Resultado:{resultado:,.2f}')

#Ainda não consegui resolver este.