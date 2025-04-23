# # promedio de 3 notas

# print("Ingresaremos las 3 notas para sacar su promedio")

# n1=int(input("Primer numero "))
# n2=int(input("Segundo numero "))
# n3=int(input("Tercer numero "))
# promedio=(n1+n2+n3)/3
# print("Su promedio es el siguiente",promedio)

# if promedio>=40:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobo")

# # verificacion de mayoria de edad

# edad=int(input("Ingrese su edad "))

# if edad>=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")


# # niño menor de 12
# # a<dolescente entre 12 y 17
# # mayor de edad más o igual a 18

# elif significa else y if en una misma palabra

# edad=int(input("Cuantos años tienes? "))

# if edad < 12:
#     print("tienes",edad, "años por lo tanto es un niño")
# elif edad >= 12 and edad <=17:
#     print("Usted es un adolescente")
# else:
#     print("Eres mayor de edad")

# ingrese 3 numeros y muestre el mayor de ellos

# n1 = int(input("Ingrese numero 1 "))
# n2 = int(input("Ingrese numero 2 "))
# n3 = int(input("Ingrese numero 3 "))

# if n1>n2 and n1>n3:
#     print("el numero", n1, "es el mayor")
# elif n2>n3:
#     print("el numero", n2, "es el mayor")
# else:
#     print("el numero", n3, "es el mayor")



# final=int(input("defina un numero para el final de su variable "))


# for hola in range (1,final+1):
#     print("Test",hola)

# es un test de tablas con el for
# print("Bienvenido a la tabla del ")

# tablas de multiplicar

# for final in range (1,11):
#     print(f"TABLA DEL: {final}")
#     for tabla in range (1,11):
#         print(f"\t{final}x{tabla}=\t",final*tabla)


# supermercado y opciones con un while y un break

# print("\tBienvenido al super de mercado\t")

# compra=input("\n\tdesea comprar algo?\n\t")


# if compra=="si":
#     print("Ha entrado al sistema de compra, estos son los productos que tenemos: ")

#     print("\n\tOpcion 1.- Baselina $5.000\n\t")

#     print("\n\tOpcion 2.- Vara magica $9.000\n\t")

#     print("\n\tOpcion 3.- Mouse barato $1.000\n\t")

    

#     total=0
   
#     while True:
#         opciones=int(input("\nescoja la opcion que mas le guste\n "))
#         if opciones==1:
#             total+=5000
#             print("\nHa seleccionado la Baselina con un costo de $5.000\n")
#         elif opciones==2:
#             total+=9000
#             print("\nha seleccionado la Varita magica con un costo de $9.000\n")
#         elif opciones==3:
#             total+=1000
#             print("\nHa seleccionado Mouse Barato con un costo de $1.000\n")
#         else:
#             print("opcion incorrecta.")
        
#         respuesta=input("\nQuiere seguir comprando? 'si' para seguir y 'no' para salir\n")  

#         if respuesta=="no":
#             print(f"\neste es su total que ha pagado:{total}\n")
#             print(f"\nY este es su total con iva:{total*1.19} \n")
#             break
# else:
#     print("ok, adios.")  