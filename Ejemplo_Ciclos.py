# Ejemplo ciclos

print("-----INICI-----")


A = ["A", "B", "C", "D", "E", "F"]

B = ["a", "b", "c", "d", "e", "f"]

for i in range(1, 7):
    for j in A:
        for z in B:
            print(str(i) + j + z)

print("---------2----------")

for i in range(1, 7):
    for j, z in zip(A, B):
        print(str(i) + j + z)

print("----------3-------------")

i = 1
L = []
while(i <= 5):
    A = int(input("Ingresa un numero: "))
    L.append(A)
    i += 1
print(L)
A = L[0]
for x in L:
    if x > A:
        A = x
print(A)


print("----FIN---")