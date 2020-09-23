def solution(X, Y, D):
    if (X == Y):
        jumps = 0
    elif Y-X % D == 0:
        jumps =int( (Y-X)/D)
    else:
        jumps = int(((Y-X)/D) + 1)
    return jumps
print(solution(10,85,30))