B = float(input("Ingrese Base:"))
A = float(input("Ingrese Altura:"))
E = float(input("Ingrese Cantidad de Estibas:"))
Ce = B*A
print("Cantidad por Estiba:", Ce)
C = Ce*E
if C>500:
 print("Excede Carga:", C)
elif C<=500:
 print("Sin problemas:", C)
