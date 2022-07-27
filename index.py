#Programa que lê número inteiro qualquer e pede para o usuário escolher uma base de conversão
num =int(input('Escolha um número inteiro qualquer:'))
base =int(input('Em qual base binária você deseja fazer a conversão? Digite:\n[1] para binário\n[2] para octal\n[3] para hexadecimal:'))
if base == 1:
    print(bin(num))
elif base == 2:
    print(oct(num))
elif base == 3:
    print(hex(num))
else:
    print('Opção inválida')
    