
contagem = 0

while(True):
    num = int(input("Digite um número: "))
    if num == 0:
        break
    
    contagem+=1
    #contagem = contagem + 1 --> enquanto eu não chegar no meu objetivo, eu vou repetir o passo
    
    print(f"Você digitou e a soma dos números digitados foi: {contagem}")
    