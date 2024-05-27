import numpy as np

rows, columns = 1000, 1000


i_tab = np.arange(rows).reshape(rows, 1)
j_tab = np.arange(columns).reshape(1, columns)

M = 2 * i_tab - j_tab

print(M)
