
# condiciones
isAdmin = False
typePlan = "Free"
saldo = 100

# if isAdmin:
#     print("es administrador!")
# else:
#     print("es invitado!")


# if isAdmin and typePlan == "PREMIUM":
#     print("es administrador!")
# else:
#     print("es invitado!")


# if typePlan == "Bussines":
#     print("plan activo")
#     if saldo < 100:
#         print("saldo insuficiente, recarga!!")

# elif typePlan == "Free":
#     print("la prueba de 7 dias temidno")
# elif typePlan == "Premium":
#     print("acceso a mas features")
# else:
#     print("welcome Invitiado")



# iteadores for

frutas = [
    "fresas",
    "peras",
    "uvas",
    "manzanas"
]

# for iterador in frutas:
#     print(iterador)
    # index = frutas.index(iterador)
    # print(index)



for iterador in enumerate(frutas):
    # index = iterador[0]
    # item = iterador[1]
    # print(index)
    # print(item)

    index, fruta = iterador
    print(index, fruta)

    # for data in iterador:
    #     pass



# for elemento in range(100):
#     print(elemento)



# while

isAdmin = True

while isAdmin:
    response = input("si desea continuar:\n ")
    if response == "no":
        break
        # isAdmin = False