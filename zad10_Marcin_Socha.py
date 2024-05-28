import numpy as np
import timeit

##### porównanie czasów

beta = [0.07,0.34]
beta0 = 0.04
dataset_size = 100000
number_of_executions = 100
x = np.random.standard_normal((dataset_size,2))

def test_equality(x):
    return x**2 + 2*x-1 == (x + 2)*x-1

def logreg_vect():
    return 1/(1 + np.exp( -(x.dot(beta)+beta0) ))

def logreg_loop():
    # Iterujemy po obserwacjach (wierszach tabeli x) za pomocą pętli for
    y_loop = np.zeros(dataset_size) # Alokacja tablicy na wyniki
    for i in range(dataset_size):
        y_loop[i] = 1/(1 + np.exp( -(x[i,:].dot(beta)+beta0) ))
  
    return y_loop

def logreg_lc():
    return [1/(1 + np.exp( -(x[i,:].dot(beta)+beta0) )) for i in range(dataset_size)]

timer1 = timeit.Timer(logreg_vect)
timer2 = timeit.Timer(logreg_loop)
timer3 = timeit.Timer(logreg_lc)

czas1 = timer1.timeit(number=1)
czas2 = timer2.timeit(number=1)
czas3 = timer3.timeit(number=1)

print(f"Czas wykonania logrec_vect: {czas1} sekund")
print(f"Czas wykonania logrec_loop: {czas2} sekund")
print(f"Czas wykonania logrec_lc: {czas3} sekund")

##### zad1
rows, columns = 1000, 1000
i_tab = np.arange(rows).reshape(rows, 1)
j_tab = np.arange(columns).reshape(1, columns)
M = 2 * i_tab - j_tab
print(M)

##### zad2
def test_equality(x):
    return x**2 + 2*x-1 == (x + 2)*x-1
