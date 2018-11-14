import sys

def input():
    return sys.stdin.readline()[:-1]

N, A = int(input()), input().split()
A.sort()
M, T = int(input()), input().split()

for m in range(M):
    if T[m] < A[0] or T[m] > A[N - 1]:
        print(0)
        continue
    left, right, find = 0, N, False
    while left < right:
        mid = int((left + right) / 2)
        if A[mid] == T[m]:
            find = True
            break
        if A[mid] < T[m]:
            left = mid + 1
        else:
            right = mid
    if find:
        print(1)
    else:
        print(0)
