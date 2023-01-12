def anioBisiesto(año):
    if año % 100 != 0:
        if año % 4 == 0:
            print("El año", año, "es bisiesto")
        else:
            print("El año", año, "NO es bisiesto")
    else:
        if año % 400 == 0:
            print("El año", año, "es bisiesto")
        else:
            print("El año", año, "NO es bisiesto")


anioBisiesto(1900)
anioBisiesto(2024)
