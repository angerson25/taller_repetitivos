numero=int(input("\nDigite un numero: "))

sumadigitos=0
digito=0
numeromodificado=numero
while numeromodificado !=0:
    digito=int(numeromodificado % 10)
    numeromodificado = (numeromodificado - digito) / 10
    sumadigitos=sumadigitos+digito

print("\nLa suma de los digitos del numero " + str(numero) + " es: " + str(sumadigitos))