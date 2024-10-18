email =input("Introduzca un Email: ")

separación = email.split("@") 

email2 = separación[0]

print(f"Tu nuevo correo será: {email2 + "@ceu.es"}")

