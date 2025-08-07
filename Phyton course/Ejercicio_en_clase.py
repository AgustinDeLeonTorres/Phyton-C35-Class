enemigo = input("¿Qué enemigo estás enfrentando? ").lower()

if enemigo == "grunt":
    print("Usa la pistola Magnum")
elif enemigo == "elite":
    print("Usa pistola de plasma + Magnum")
elif enemigo == "hunter":
    print("Usa la escopeta")
elif enemigo == "flood":
    print("Usa el lanzallamas")
elif enemigo == "muy lejos":
    print("Usa el francotirador")
elif enemigo == "tanque":
    print("Usa el lanzacohetes")
else:
    print("Usa cualquier arma disponible")