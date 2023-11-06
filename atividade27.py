# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES.
palavra = str(input("Digite uma palavra: "))
for nome in palavra:
    plvrfnl = palavra[::-1]
    if plvrfnl == palavra:
        print(palavra, "é palíndromo!")
    else:
        print(palavra, "não é palíndromo!")