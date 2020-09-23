A=[3,4,4,6,1,4,4]
N=5
def solution(N,A):
    counters = [0]*N
    max_1 =0
    for x in A:
        if 1<=x<=N:
            counters[x-1]+=1
            if counters[x-1]>max_1:
                max_1= counters[x-1]
        else:
            counters=[max_1]*N
    return counters
print(solution(N,A))
