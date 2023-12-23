N, K = map(int, input().split())

arrays = []

for i in range(2):
    arrays.append(list(map(int, input().split())))
    
A = arrays[0]
B = arrays[1]

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))