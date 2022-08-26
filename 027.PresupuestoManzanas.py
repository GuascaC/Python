C = float(input("Ingrese cantidad de Manzanas:"))
P = float(input("Ingrese Precio de Manzanas:"))
T = C*P
if T<=3000:
 print("Dentro de presupuesto:", T)
elif T>3000:
 print("Fuera de presupuesto:", T)
