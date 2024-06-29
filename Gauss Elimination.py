import math

def gausselim(A):
    n = len(A)
    # Forward elimination
    for i in range(n-1):
        # find Pivot
        p = -1
        for k in range(i, n):
            if A[k][i] != 0:
                p = k
                break

        if p == -1:
            print('No unique solution exists')
            return None

        if p != i:
            A[i], A[p] = A[p], A[i]

        # Elimination
        for j in range(i+1, n):
            if A[i][i] == 0:
                continue
            Mji = A[j][i] / A[i][i]
            for k in range(i, n+1):
                A[j][k] = A[j][k] - Mji * A[i][k]

    if A[n-1][n-1] == 0:
        print("No unique solution exists")
        return None

    # Back substitution
    x = [0.0] * n
    x[n-1] = A[n-1][n] / A[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum_ai = sum(A[i][j] * x[j] for j in range(i+1, n))
        if A[i][i] == 0:
            print("No unique solution exists due to division by zero")
            return None
        x[i] = (A[i][n] - sum_ai) / A[i][i]

    return x

# Define the augmented matrix
A = [
    [math.pi, math.sqrt(2), -1, 1, 0],
    [math.e, -1, 1, 2, 1],
    [1, 1, -math.sqrt(3), 1, 2],
    [-1, -1, 1, -math.sqrt(5), 3]
]

# Solve the system using Gaussian elimination
solution = gausselim(A)

# Print the solution
if solution:
    print("Solution:", solution)


x1 = 1.3494485582070679
x2 = -4.677987751108763
x3 = -4.032893778689474
x4 = -1.65663773331691

# Verify each equation
eq1 = math.pi * x1 + math.sqrt(2) * x2 - x3 + x4
eq2 = math.e * x1 - x2 + x3 + 2 * x4
eq3 = x1 + x2 - math.sqrt(3) * x3 + x4
eq4 = -x1 - x2 + x3 - math.sqrt(5) * x4

print(eq1, eq2, eq3, eq4)


A = [
    [math.pi, math.sqrt(2), -1, 1, 0],
    [math.e, -1, 1, 2, 1],
    [1, 1, -math.sqrt(3), 1, 2],
    [-1, -1, 1, -math.sqrt(5), 3]
]
