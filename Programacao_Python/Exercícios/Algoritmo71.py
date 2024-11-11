'''Criar um algoritmo que leia um valor de hora e informe quantos minutos se passaram 
desde o início do dia.'''

hora = float(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
minutosPassados = (hora * 60) + minutos

print(f"Passaram-se {minutos} desde o início do dia até agora")