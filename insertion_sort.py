A = [5, 2, 4, 6, 1, 3]
print(A)

for j in range(1, len(A)):
    chave = A[j]
    # Inserir A[j] na sequência ordenada A[1..j-1]
    i = j - 1
    
    while i >= 0 and A[i] > chave:
        A[i + 1] = A[i]
        i = i - 1
    
    A[i + 1] = chave
print(A)
