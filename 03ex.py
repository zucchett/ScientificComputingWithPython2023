#esercizio 1
print("Esercizio 1\n")

def convert_num(n, tipo):
    if isinstance(n, int):
        if tipo=="dec":
            print("The number", n, "in decimal is:", n)
        elif tipo=="hex":
            print("The number", n, "in hexadecimal is:", hex(n))
        elif tipo=="bin":
            print("The number", n, "in binary is:", bin(n))
        else:
            print("Invalid input!")
    elif isinstance(n, str):
        if n[1]=="b":
            x=int(n, 2)
        elif n[1]=="x":
            x=int(n, 16)
        else:
            "Invalid input!"    
        if isinstance(x, int):
            if tipo=="dec":
                print("The number", n, "in decimal is:", x)
            elif tipo=="hex":
                print("The number", n, "in hexadecimal is:", hex(x))
            elif tipo=="bin":
                print("The number", n, "in binary is:", bin(x))
            else:
                print("Invalid input!")
        else:
            print("Conversion error!")
convert_num("0b1011", "hex")

#esercizio 2
print("\nEsercizio 2\n")
Nbin="01000101010110000000000000000000"
segno=int(Nbin[0], 2)
espo=int(Nbin[1:9], 2)
mant=int(Nbin[9:], 2)
den=1
while den<=mant:
    den=den*10
mant=mant/den
Ndec=((-1)**segno)*(1+mant)*(2**(espo-127))
print(Ndec)

#esercizio 3
print("\nEsercizio 3\n")
upper=1.0
lower=1.0
while upper*2!=float('inf'):
    upper=upper*2
while lower/2!=0.0:
    lower=lower/2
print("Highest number:", upper,"\nSmallest fraction:", lower)

#esercizio 4
print("\nEsercizio 4\n")
test=1.0
while 1.0+test!=1.0:
    test=test/2
print("Smallest precision:", test)

#esercizio 5
print("\nEsercizio 5\n")

#esercizio 6
print("\nEsercizio 6\n")

#esercizio 7
print("\nEsercizio 7\n")
