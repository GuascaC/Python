V = float(input("Ingrese preguntas correctas:"))
P = float(input("Ingrese total preguntas:"))
X1=50/P
X2=X1*V
print("Parcial:",X2)
A = float(input("ingrese nota actividad"))
X3=(A*0.30)+(X2*0.70);
print("Total:", X3)
