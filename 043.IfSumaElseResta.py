a=float(input("Ingrese un número entero:"))    
b=float(input("Ingrese un otro:"))    
c=float(input("Ingrese uno más:"))
if (a>=0 and b>=0 and c>=0):
    if(a>b):
     r=a-b
     d=a-b
     print ("Diferencia:",r,"División:",d)
    else:
     s=a+b
     m=a*b
     print ("Suma:",s,"Multiplicación:",m)
else:
  print("Ingrese un número entero")
