print('Jogo da adivinhação, adivinhe a palavra secreta, dica: comida,\
Lembrando, não use sinais tais como "´^~"')


palavra_secreta='feijao'
print(f'você pode tentar {len(palavra_secreta)+ 7} vezes')
letras_acertadas=''
tentativas=0
while True:
    if tentativas == len(palavra_secreta) + 7:
        print('Você Ultrapassou o limite de tentativas')
        print(f'você tentou: {tentativas} vezes')
        break

    letra_digitada=input('digite uma letra para verificar se ela se encontra dentre as letras da palavra secreta: ')
    tentativas+=1
    
    if len(letra_digitada) >1:
        print('digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada=''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada+=letra_secreta
        else:
            palavra_formada+= '*'
    print(' a palavra formada é: ',palavra_formada)

    if palavra_formada== palavra_secreta:
        print('VOCÊ GANHOUUU!')
        print( 'a palavra era:',palavra_secreta)
        print('você tentou', tentativas, 'vezes')
        tentativas=0
        letras_acertadas=''