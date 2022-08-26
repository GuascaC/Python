import math
r=0.0
x=0.0
y=0.0
print("\t\t\tUbicar Punto en el Plano Cartesiano")

x=float(input("\nPor favor ingrese el valor de x\n"))
y=float(input("\nPor favor ingrese el valor de Y\n"))
r=float(input("\nPor favor ingrese el valor del radio\n"))
if x > 0 and y > 0 :
  print("El punto se encuentra en el primer cuadrante del plano cartesiano")
if x < 0 and y > 0 :
  print("El punto se encuentra en el segundo cuadrante del plano cartesiano")
if x < 0 and y < 0 :
  print("El punto se encuentra en el tercer cuadrante del plano cartesiano")
if x > 0 and y < 0 :
  print("El punto se encuentra en el cuarto cuadrante del plano cartesiano")
if x == 0 and y==0 :
  print("El punto se encuentra en el punto de origen")
if x == 0 or y==0 :
  if x!=0 :
    print("El punto se encuentra sobre el eje x")
  if y!=0 :
     print("El punto se encuentra sobre el eje y")
if x==y :
  print("El punto se encuentra sobre la grafica y=x")
if x < y :
  print("El punto se encuentra encima de la gráfica y=x")
if x > y :
  print("El punto se encuentra debajo de la gráfica y=x")
htp=((x*x)+(y*y))
largo_punto=math.sqrt(htp)
if largo_punto>r :
  print("El punto está fuera de la circunferencia")
if largo_punto<r :
  print("El punto está dentro de la circunferencia")
if largo_punto==r :
  print("El punto está sobre el borde de la circunferencia")