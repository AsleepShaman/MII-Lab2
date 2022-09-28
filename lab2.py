import numpy as np
import matplotlib.pyplot as plt

K = int(input("Введите число K: "))
N = int(input("Введите число N(больше 3 и кратное 2): "))

if N < 4 or (N % 2 != 0):
    print("N не корректна!")
    exit()

N = N // 2

b = np.random.randint(-10, 10, (N, N))
c = np.random.randint(-10, 10, (N, N))
d = np.random.randint(-10, 10, (N, N))
e = np.random.randint(-10, 10, (N, N))

A = np.vstack([np.hstack([e, b]), np.hstack([d, c])])
print("Матрица A:")
print(A, '\n')

F = A.copy()

countP = 0
countO = 0
for i in c:
    for j in i[1::2]:
        if j > 0:
            countP += 1
            
for i in c:
    for j in i[::2]:
        if j < 0:
            countO += 1
            

print("Положительных элементов в четных столбцах: ",countP)
print("Отрицательных элементов в нечетных столбцах: ",countO, "\n")

if countP > countO:
    cf = np.flip(c, 0)
    bf = np.flip(b, 0)
    F = np.vstack([np.hstack([e, cf]), np.hstack([d, bf])])
else:
    F = np.vstack([np.hstack([c, b]), np.hstack([d, e])])

print("Матрица F:")
print(F, '\n')

if np.linalg.det(A) > np.diagonal(F).sum():
    result = A * np.transpose(A) - K * np.linalg.inv(F)
else:
    result = (np.linalg.inv(A) + np.tril(A) - np.linalg.inv(F)) * K
 
print("Результ вычислений:")
print(result)

fig = plt.figure(figsize=(9, 3))
plt.subplot(131)
pc = plt.contourf(F)

plt.subplot(132)
pc = plt.pcolor(F)

plt.subplot(133)
pc = plt.contour(F)

plt.show()