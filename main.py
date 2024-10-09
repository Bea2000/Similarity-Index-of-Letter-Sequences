# Obtiene N desde standard input
N = int(input())

ans = 0

A = []

# Obtiene cada A_i desde standard input
for i in range(N):
  s = input()
  A.append(s)

def encontrar_lexico_menor(A):
    if len(A) % 2 == 1:
        return A
    else:
        middle = len(A)//2
        A_1 = encontrar_lexico_menor(A[:middle])
        A_2 = encontrar_lexico_menor(A[middle:])
        if A_1 < A_2:
            return A_1 + A_2
        else:
            return A_2 + A_1

for i in range(N):
    for j in range(i+1, N):
        if encontrar_lexico_menor(A[i]) == encontrar_lexico_menor(A[j]):
            ans += 1
  

print(ans)

