import sys
input = sys.stdin.readline
N = int(input())
A, D = [0 for _ in range(N + 2)], [0 for _ in range(N + 2)]

for i in range(N):
    A[i] = int(input())

D[0], D[1] = A[0], A[0] + A[1]
D[2] = max(A[0] + A[2], A[1] + A[2], D[1])

for i in range(3, N):
    D[i] = max(D[i - 1], D[i - 2] + A[i], D[i - 3] + A[i - 1] + A[i])

print(D[N - 1])
