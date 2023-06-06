#Comprobar vocales

letra = input("Digite un caracter: ").lower()

if letra=='a' or  letra== 'e' or letra== 'i' or letra=='o' or letra=='u':
    print("Es una vocal")
else:
    print("No es una vocal")    
    
    
# Otra forma de hacerlo pero en lugar del lower usar el upper

letra = input("Digite un caracter: ").upper()

if letra=='A' or  letra== 'E' or letra== 'I' or letra=='O' or letra=='U':
    print("Es una vocal")
else:
    print("No es una vocal")    
