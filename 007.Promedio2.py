n1=float(input("ingrese Nota 1: "))
n2=float(input("ingrese Nota 2: "))
n3=float(input("ingrese Nota 3: "))
notaf= (n1*10/100)+(n2*60/100)+(n3*30/100)
print("la nota definitiva es: ")
print (notaf)
if notaf >= 30:
    print("aprobó")
else:
    print("no aprobó")
