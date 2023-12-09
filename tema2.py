

#Ex1
def my_sum (*args, **kwargs):
    suma=0
    for i in args:
        try:
            suma += i
        except TypeError:
            pass
    return suma

print (my_sum(1,5,-3,'abc', [12,56,'cad']))
print(my_sum())
print(my_sum(2,4,'abc',param_1=2))



#Ex2

def suma_recursiva(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])

print("suam numerelor: ", suma_recursiva([1,2,3,4,5]))

def suma_recursiv_par(lista):
    if not lista:
        return 0
    else:
        suma = lista[0] if lista[0] % 2 == 0 else 0
        return suma + suma_recursiv_par(lista[1:])

print("suma numerelor pare: ",suma_recursiv_par([1,2,3,4,5,6,7,8]))


def suma_recursiv_impar(lista):
    if not lista:
        return 0
    else:
        suma = lista[0] if lista[0] % 2 == 1 else 0
        return suma + suma_recursiv_impar(lista[1:])

print("suma numerelor impare: ",suma_recursiv_impar([1,2,3,4,5,6,7,8]))



#Ex3


n = input("Introduceti un numar de la tastatura: ")
try:
    intreg = int(n)
except ValueError as e:
    print(0)
else:
    print(intreg)