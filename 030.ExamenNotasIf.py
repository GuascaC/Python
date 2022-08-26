V = float(input("Ingrese preguntas correctas:"))
P = float(input("Ingrese total preguntas:"))
X1=50/P
X2=X1*V
print("Parcial:",X2)
A = float(input("ingrese nota actividad:"))
X3=(A*0.30)+(X2*0.70);
if X3>=30:
 print("Pasa,Nota:",X3)
elif X3<30:
 print("No pasa,Nota:", X3)
