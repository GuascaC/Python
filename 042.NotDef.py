n=1
while (n<=16):
 nota1=float(input("Ingrese nota 1:"))    
 nota2=float(input("Ingrese nota 2:"))    
 nota3=float(input("Ingrese nota 3:"))    
 nota4=float(input("Ingrese nota 4:"))    
 nota5=float(input("Ingrese nota 5:"))    
 notadefinitiva=(nota1*0.10)+(nota2*0.20)+(nota3*0.30)+(nota4*0.10)+(nota5*0.30)
 if (notadefinitiva>=30):
    print("Aprobó!:",notadefinitiva)
 else:
  print("Necesita un curso de recuperación:",notadefinitiva)
n=n+1
