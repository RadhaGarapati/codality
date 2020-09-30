def Solution(S, P, Q):
    key = {"A": 1, "C": 2, "G": 3, "T": 4}
    new_arr = []
    for i in range(len(P)):
        for x in key:
            if x in S[P[i] : Q[i] + 1]:
                new_arr.append(key[x])
                break
    return new_arr
