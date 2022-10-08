cheque=int
cantbilletesdosmil=0
cantbilletesdiezmil=0
cantmonedascien=0
while cheque != 0:
    cheque=int(input("\nDigita el valor del cheque: "))
    billetesdiezmil=cheque//10000
    billetesdosmil=(cheque-(billetesdiezmil*10000))//2000
    monedascien=(cheque-(billetesdiezmil*10000)-(billetesdosmil*2000))//100

    print("\nPara el cheque de " + str(cheque) + " se entregan: \n" + str(billetesdiezmil) + " billetes de diez mil; " + str(billetesdosmil) + " billetes de dos mil y " + str(monedascien) + " monedas de cien.")

    cantbilletesdiezmil= cantbilletesdiezmil + billetesdiezmil
    cantbilletesdosmil=cantbilletesdosmil + billetesdosmil 
    cantmonedascien=cantmonedascien + monedascien

print("\nDurante el dia se entregaron: \n"+ str(cantbilletesdiezmil) + " billetes de diez mil; " + str(cantbilletesdosmil) + " billetes de dos mil y " + str(cantmonedascien) + " monedas de cien.")

