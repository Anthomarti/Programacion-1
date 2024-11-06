A = matrix(c(2, 3, -1, 1, 1, 1, 1, -3, 2), ncol = 3, byrow = T)
A

b = c(1, 2, 3)
x = solve(A, b)
x

# verificación
A%*%x