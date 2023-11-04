def gauss(n, a, b):
    for i in range(n):
        if a[i][i] == 0.0:
            return Exception
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n):
                a[j][k] = a[j][k] - ratio * a[i][k]
            b[j] = b[j] - ratio * b[i]
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
    return x

a = [[3, -4, -2, 4], 
     [6, -6, 1, 7], 
     [-3, 2, 2, 2]]
b = [4, 7, 2]

print("Результат: ", gauss(3, a, b))
