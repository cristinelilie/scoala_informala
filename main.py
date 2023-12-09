
#declarare lista
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# lista ordonata ascendent
print(sorted(lista))

#lista ordonata descendent
print(sorted(lista,reverse=True))

#numere cu indici pari
print(lista[::2])

#numere cu indici impari
print(lista[1::2])

#elemente multipli de 3
print([x for x in lista if x%3 ==0])
