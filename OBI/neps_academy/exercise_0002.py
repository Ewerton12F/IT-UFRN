a = int(input())
b = int(input())
c = int(input())

A = [a, b, c]
O = A[:]
podium = []

for j in range(1, len(A)):
    chave = A[j]
    # Inserir A[j] na sequência ordenada A[1..j-1]
    i = j - 1
    while i >= 0 and A[i] > chave:
        A[i + 1] = A[i]
        i = i - 1
    
    A[i + 1] = chave

for x in range(0, len(A)):
    for y in range(0, len(O)):
        if A[x] == O[y]:
            podium.append(y + 1)

for z in podium:
    print(z)