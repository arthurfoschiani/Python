n = 30
ultimo=1
penultimo=1

print("0")
print("1")
print("1")
count=3
while count <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    print(termo)