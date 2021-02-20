def repeatedNTimes(A: list) -> int:
        A.sort()
        for i in range(len(A)):
            if A[i] == A[i+1]:
                return A[i]

A =  [1,2,3,3]
print(A, repeatedNTimes(A))
