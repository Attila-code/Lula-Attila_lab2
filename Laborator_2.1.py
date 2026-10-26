print(" Cerinta 1 ")
text_sir = input("Baga numerele pentru sir, separate prin spatiu: ")
sir = []
for x in text_sir.split():
    sir.append(int(x))
print("Sirul citit este:", sir)

randuri = int(input("Cate randuri are matricea? "))
coloane = int(input("Cate coloane? "))
matrice = []

for i in range(randuri):
    rand_nou = []
    for j in range(coloane):
        valoare = int(input("Elementul de pe pozitia " + str(i) + "," + str(j) + ": "))
        rand_nou.append(valoare)
    matrice.append(rand_nou)

print("Matricea arata asa:")
for rand in matrice:
    print(rand)

