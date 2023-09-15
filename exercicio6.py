# Exercicio 007
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
largura = float( input('Insira a largura:'))
comprimento = float( input('Insira o comprimento:'))
resultado = (largura * comprimento * 2)

print (f'Resultado:{resultado:,.2f} m²')