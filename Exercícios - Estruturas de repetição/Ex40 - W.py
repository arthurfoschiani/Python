n = 20
ultimo=1
penultimo=1
anti = 1

print("0")
print("1")
print("1")
print("1")
count=1
while count <= n:
    termo = ultimo + penultimo + anti
    anti = penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    print(termo)