cp1=float(input("Ingrese cantidad 1"))
cp2=float(input("Ingrese cantidad 2"))
cp3=float(input("Ingrese cantidad 3"))
vp1=float(input("Ingrese valor 1"))
vp2=float(input("Ingrese valor 2"))
vp3=float(input("Ingrese valor 3"))
tp=((cp1*vp1)+(cp2*vp2)+(cp3*vp3))
if tp<=25000:
 print ("No tiene descuento,Total:",tp)
else:
  print ("Tiene 10 %")
  d=tp*0.10
  tp2=tp-d
  print("descuento:",d)
  print("Total:",tp2)
