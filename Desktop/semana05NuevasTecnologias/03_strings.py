#desempaquetar un string
# lenguaje = "python"
# a,b,c,d,e,f = lenguaje
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

#acceder por indie 
# primera_letra = lenguaje[0]
# otra_letra = lenguaje[3]
# print(primera_letra , otra_letra)

# ultima_letra = lenguaje[5]
# otra_letra1 = lenguaje[-1]#el menos se utilizapara encontrar el ultimo caracter sin saber el final


# print(len(lenguaje))
# #rebanada de string
# prime_tercera = lenguaje[0:3]#los : significan desde 
# print(prime_tercera)

# ultimo_tercero = lenguaje [-3: ]
# print(ultimo_tercero)


#que vaya  en 2 en 2
# pto = lenguaje[0:6:2]#inicio,final,salto
# print(pto)

#capitallize()pasar letra en mayuscula
nuestro_reto = "aprender python este semestre"#pasa la primera letra en mayuscula 
# print(nuestro_reto.capitalize())

#title()psar  la letra de cada palabra en mayuscula
print(nuestro_reto.title())#pasa cada comienzo de una palabra en mayuscula ejem:Hola Como Estas
#count() contar caracteres especificos
print(nuestro_reto.count("e"))#cuantas veces aparece una letra en un texto
print(nuestro_reto.count("th"))

#endswith() verificar si la frase termina en una cadena especifica
print(nuestro_reto.endswith("tre"))
print(nuestro_reto.endswith("to"))

#find()buscar algo especifico en la cadena 
print(nuestro_reto.find("w"))
print(nuestro_reto.find("p"))

#isalnum verefica si es alfanumerico 
print(nuestro_reto.isalnum())
#isapha si es una letra del alfabeto
print(nuestro_reto.isalpha())
#isdecimal si es un decimal
print(nuestro_reto.isdecimal())
#isdigit si un digito del 0 al 9 
print(nuestro_reto.isdigit())


#ejemplo
edad = input("ingresa tu edad")
if edad.isdigit():
    print(type(edad))
    edad=int(edad)
    print(type(edad))

else:
    print("porfavor ingrese solo numeros ")

#isidentifier si es algo valido para ser un identificador


















        
        
    
        
        


    
 

