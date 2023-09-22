# Ejemplos Comprension de Lista

print("-----------INICIO--------")

lista = [letra for letra in 'casa']
print(lista)

A = [5, 96, 785, 852, 558, 45, 1012]

L = [i for i in A if i > 500]
print(L)

B = [i for i in range(1, 101) if i % 2 == 0]
print(B)

lista = [numero for numero in
            [numero**2 for numero in range(0,11)]
                if numero % 2 == 0 ]
print(lista)


print("-----------FIN-----------")