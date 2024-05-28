import numpy as np

##### zad1
rows, columns = 1000, 1000
i_tab = np.arange(rows).reshape(rows, 1)
j_tab = np.arange(columns).reshape(1, columns)
M = 2 * i_tab - j_tab
print(M)

##### zad2
def test_equality(x):
    return x**2 + 2*x-1 == (x + 2)*x-1
