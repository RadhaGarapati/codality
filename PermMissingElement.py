def solution(A):
    N = len(A)
    diff = ((N + 1) * (N + 2))/2 - sum(A)
    if diff == 0:
        return(N+1)
    else:
        return(diff)

if __name__ == '__main__':
    A = [2, 3, 1,5,]
    print(solution(A))