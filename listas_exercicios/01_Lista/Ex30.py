# Escreva um programa que peça ao usuário para digitar sua altura em metros (ex: 1.75) 
# e seu peso em quilogramas (ex: 68.5). 
# Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura * altura) 
# e imprima o resultado formatado com duas casas decimais.
altura=float(input("Qual é a sua altura?\n"))
peso=float(input("Qual é o seu peso?\n"))
imc=peso/(altura*altura)
print(f"O seu IMC é: {imc:.2f}")