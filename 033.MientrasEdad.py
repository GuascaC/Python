c=4
while c<=6:
 n1 = float(input("Ingrese año de nacimiento : "))
 n = 2022-n1
 c=c+1
 if n>=18:
     print ("Mayor de edad,")
 elif n<18:
     print ("Menor de edad,")
 print (n)
