personas = []

try:
    with open("agenda.txt", "r") as f_agenda:
        lineas = f_agenda.readlines()
        for linea in lineas:
            if linea.strip():
                partes = linea.strip().split(" Edad: ")
                if len(partes) > 1:
                    nombre_apellido = partes[0].split()
                    nombre = nombre_apellido[0]
                    apellido = nombre_apellido[1] if len(nombre_apellido) > 1 else ""
                    
                    resto = partes[1].split(" Correo: ")
                    edad = int(resto[0])
                    
                    correo_telefono = resto[1].split(" Telefono: ")
                    correo = correo_telefono[0]
                    telefono = correo_telefono[1] if len(correo_telefono) > 1 else ""
                    
                    personas.append([nombre, apellido, edad, correo, telefono])
except FileNotFoundError:
    print("Archivo agenda.txt no encontrado. Comenzando agenda vacía.")
except Exception as e:
    print(f"Error leyendo archivo: {e}")

while True:
    print("\nAGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Modificar contacto")
    print("4. Guardar y salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        contacto = []
        while True:
            nombre = input("Introduce tu nombre: ")
            apellido = input("Introduce tu apellido: ")
            if nombre == "":
                print("No has introducido tu nombre")
            elif apellido == "":
                print("No has introducido tu apellido")
            else:
                contacto.append(nombre)
                contacto.append(apellido)
                break

        while True:
            try:
                edad = int(input("Introduce tu edad: "))
                contacto.append(edad)
                break
            except ValueError:
                print('Debes introducir un número')

        correo = input("Introduce tu correo: ")
        contacto.append(correo)

        while True:
            try:
                telefono = input("Introduce tu telefono: ")
                int(telefono)
                contacto.append(telefono)
                break
            except ValueError:
                print('Debes introducir un número')

        personas.append(contacto)
        print("Contacto agregado correctamente")

    elif opcion == "2":
        if not personas:
            print("No hay contactos en la agenda")
        else:
            print("\n--- LISTA DE CONTACTOS ---")
            for i, persona in enumerate(personas, 1):
                print(f"{i}. {persona[0]} {persona[1]} - Edad: {persona[2]} - Correo: {persona[3]} - Teléfono: {persona[4]}")

    elif opcion == "3":
        if not personas:
            print("No hay contactos para modificar")
            continue
            
        print("\n--- CONTACTOS DISPONIBLES ---")
        for i, persona in enumerate(personas, 1):
            print(f"{i}. {persona[0]} {persona[1]}")

        while True:
            try:
                num_contacto = int(input("\n¿Qué contacto deseas modificar? (número): ")) - 1
                if 0 <= num_contacto < len(personas):
                    break
                else:
                    print(f"Por favor, ingresa un número entre 1 y {len(personas)}")
            except ValueError:
                print("Debes introducir un número válido")

        contacto = personas[num_contacto]
        print(f"\nModificando contacto: {contacto[0]} {contacto[1]}")
        
        while True:
            print("\n¿Qué dato deseas modificar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Edad")
            print("4. Correo")
            print("5. Teléfono")
            print("6. Volver al menú principal")
            
            campo = input("Elige una opción: ")
            
            if campo == "1":
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre:
                    contacto[0] = nuevo_nombre
                    print("Nombre actualizado correctamente")
                else:
                    print("El nombre no puede estar vacío")
                    
            elif campo == "2":
                nuevo_apellido = input("Nuevo apellido: ").strip()
                if nuevo_apellido:
                    contacto[1] = nuevo_apellido
                    print("Apellido actualizado correctamente")
                else:
                    print("El apellido no puede estar vacío")
                    
            elif campo == "3":
                while True:
                    try:
                        nueva_edad = int(input("Nueva edad: "))
                        if nueva_edad > 0:
                            contacto[2] = nueva_edad
                            print("Edad actualizada correctamente")
                            break
                        else:
                            print("La edad debe ser un número positivo")
                    except ValueError:
                        print("Debes introducir un número válido")
                        
            elif campo == "4":
                nuevo_correo = input("Nuevo correo: ").strip()
                if nuevo_correo:
                    contacto[3] = nuevo_correo
                    print("Correo actualizado correctamente")
                else:
                    print("El correo no puede estar vacío")
                    
            elif campo == "5":
                while True:
                    try:
                        nuevo_telefono = input("Nuevo teléfono: ").strip()
                        if nuevo_telefono:
                            int(nuevo_telefono)
                            contacto[4] = nuevo_telefono
                            print("Teléfono actualizado correctamente")
                            break
                        else:
                            print("El teléfono no puede estar vacío")
                    except ValueError:
                        print("Debes introducir un número válido")
                        
            elif campo == "6":
                break
            else:
                print("Opción no válida. Por favor, elige entre 1-6")

    elif opcion == "4":
        with open("agenda.txt", "w") as f_agenda:
            for persona in personas:
                f_agenda.write(f'{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}\n')
        print("Datos guardados en agenda.txt. ¡Hasta pronto!")
        break
        
    else:
        print("Opción no válida. Por favor, elige entre 1-4")