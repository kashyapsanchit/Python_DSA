def two_sum(A, target):
    i = 0
    j = len(A) - 1

    while i <= j:
        if A[i] + A[j] == target:
            return True
        else:
            i += 1
    return False

A = [1, 2, 5, 6]
target = 10

print(two_sum(A, target))