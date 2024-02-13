#while...break
i=0 #valor inicial
while i<=10:#condição
  if i==4:
    break
  print(i,end=" ")
  i+=1 #contador
print("\nContinua...")

i=4 #valor inicial
while i<=10:#condição
  print(i,end=" ")
  if i==4:
    break
  i+=1 #contador
print("\nContinua...")

j=79
while j<=90:
  print(j)
  if j==81:
    break
  j+=2
print("Fim do looping")

k=0
while True:
  print(k,end=" ")
  if k==7:
    break
  k+=1
print ("\nFim do looping")
\
soma=0
while True:
  num=int(input("Digite um número ou 0 para sair: "))
  print(f"Numero digitado {num}")
  soma+=num
  if num==0:
    break
print(f"A soma dos valores: {soma}")

for i in range(12):
    print(i,end=" ")

for x in range(6,11,3):
  print(x, end=" ")

  for a in "Prova":
    print(a)