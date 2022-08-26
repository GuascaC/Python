h=float(input("Ingrese Horas:"))
m=float(input("Ingrese Minutos:"))
if m>=0:
 h=h+1
else:
 print("Minutos negativos")
p=h*2500
print("Pago:",p)
