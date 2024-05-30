##### Ex 3

t = d2.groupby(['Exp id'])['Objective Function'].agg('std')
#skoro chcemy, aby dane były różne, to wówczas
#std == 0
t2 = t[t != 0]
t3 = d2[d2['Exp id'].isin(t2.index)]


##### Ex 4

t4 = d2[~d2.index.isin(t3.index)]
t5 = t4.groupby(['Exp id'])['Objective Function'].agg('std')
max(t5 / np.sqrt(2)) #ponieważ wiemy, że mamy dokładnie dwie dane zawsze,
                     #więc dla std wystarczy podzielić wynik, przez sqrt(2)
