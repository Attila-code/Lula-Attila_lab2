print("\n Cerinta 2 ")
nume_fisier = input("Cum se numeste fisierul de unde citim? ")

try:
    fisier = open(nume_fisier, "r")
    text_fisier = fisier.read()
    fisier.close()

    sir_fisier = []
    for x in text_fisier.split():
        sir_fisier.append(int(x))
    print("Sirul gasit in fisier este:", sir_fisier)
except:
    print("Eroare: Fisierul nu exista!")