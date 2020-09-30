def Solution(K):
    A = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    if len(A) == 0:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K]


print(Solution(4))
