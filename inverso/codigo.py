numero=int(input("\nDigite un numero: "))

while numero < 1:
    print("Numero invalido")
    numero=int(input("\nDigite un numero: "))

numeromodificado=numero
contador=0

while numeromodificado // 10**contador != 0:
    contador=contador+1

inversohipotetico=0

while contador != 0:
    digito= (numeromodificado%10)*10**contador
    numeromodificado = (numeromodificado - digito)// 10
    inversohipotetico = inversohipotetico + digito
    contador = contador - 1

inverso=inversohipotetico//10

print("El inverso del numero "+ str(numero) + " es: "+ str(inverso))
