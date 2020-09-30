A = [3, 1, 2, 4, 3]


def solution(A):
    chop1 = A[0]
    chop2 = sum(A[1:])
    min_diff = abs(chop1 - chop2)
    for i in range(1, len(A) - 1):
        chop1 += A[i]
        chop2 -= A[i]
        if abs(chop1 - chop2) < min_diff:
            min_diff = abs(chop1 - chop2)
    return min_diff


print(solution(A))
