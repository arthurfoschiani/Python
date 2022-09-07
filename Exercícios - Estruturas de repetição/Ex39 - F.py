ultimo=1
penultimo=1

print("0")
print("1")
print("1")
for count in range(3, 31, 1):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print(termo)