C = float(input("Ingrese cantidad de Manzanas:"))
P = float(input("Ingrese Precio de Manzanas:"))
T = C*P
print("Total Manzanas:", T)
Cp = float(input("Ingrese cantidad de Peras:"))
Pp = float(input("Ingrese Precio de Peras:"))
Tp = Cp*Pp
if Pp>800:
 print("Muy caro,total:", Tp)
elif Pp<800:
 print("Barato,total:", Tp)
T=T+Tp
if T<5000:
 print("Dentro de presupuesto:", T)
elif T>5000:
 print("Fuera de presupuesto:", T)
