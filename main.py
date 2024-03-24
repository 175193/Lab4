import numpy as np

# a = np.arange(2, dtype='int32')
# print(a)
# print(a.dtype)
# print(a.shape)
# print(a.ndim)
#
# b = a.astype('float')
# print(b.dtype)
#
# m = np.array((np.arange(2), np.arange(2)))
# print(m)
# print(m.shape)
# print(m.ndim)

# macierz = np.array(([1, 2], [3, 4], [5, 6]))
# print(macierz)
# print(macierz.shape)

# zera = np.zeros([5, 5])
# jedynki = np.ones([4, 4])
# print(zera)
# print(jedynki)
#
# pusta = np.empty([2, 2])
# print(pusta[1, 0])

# liczby = np.arange(1, 2, 0.1)
# print(liczby)
#
# liczby_lin = np.linspace(1, 2, 10, endpoint=False)
# print(liczby_lin)

# z = np.indices((5, 3))
# print(z)
# print(z[0][0][0])

# x, y = np.mgrid[0:5, 0:5]
#
# print(x)
# print(y)

# diag = np.diag([x for x in range(5)], k=0)
# print(diag)
#
# z = np.fromiter(range(5), dtype='int32')
# print(z)

# znaki = b'abcdef'
#
# zn1 = np.frombuffer(znaki, dtype='S1') # S1 = 1 długość stringa
# zn2 = np.frombuffer(znaki, dtype='S2')
# print(zn1)
# print(zn2)

# znaki = 'abcdef'
#
# zn1 = np.array(list(znaki))
# zn2 = np.array(list(znaki), dtype='S')
# zn3 = np.array(list(b'abcdef'))
# zn4 = np.fromiter(znaki, dtype='S1')
# zn5 = np.fromiter(znaki, dtype='U1')
#
# print(zn1)
# print(zn2)
# print(zn3)
# print(zn4)
# print(zn5)

# mat = np.array([[2, 2], [2, 2]])
# mat1 = np.array([[3, 4], [5, 6]])
# print(mat + mat1)
# print(mat - mat1)
# print(mat.dot(mat1))
# print(mat1.dot(mat))
# print(mat / mat1)

# a = np.arange(10)
# print(a)
#
# s = slice(2, 7, 2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:])
# print(a[2:5])

# mat = np.arange(25)
# mat = mat.reshape([5, 5])
# print(mat)
# print(mat[1:])
# print(mat[:, 1:])


# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
#rows = np.array([[0, 0], [3, 3]])
#cols = np.array([[0, 2], [0, 2]])

#y = [rows, cols]
#print(y)

# zad 1
arr = np.arange(0, 45, 3)
print(arr)

# zad 2
arr = np.array([1, 2, 3, 5, 6], dtype='float')
arr1 = arr.astype('int64')
