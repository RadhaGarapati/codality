def Solution(A):
    odd = 0
    for i in A:

        odd ^= i
    return odd


print(Solution([9, 7, 7, 9, 3, 4, 4]))
