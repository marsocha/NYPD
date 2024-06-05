import pandas as pd

leadername = ['Stanisław', 'Jan', 'Jan', 'Grzegorz', 'Jan']
leadersurname = ['Żółkiewski', 'Chodkiewicz', 'Sobieski', 'Chodkiewicz', 'Chodkiewicz']
battle = ['Kłuszyn 4.VII.1610', 'Kircholm 27.IX.1605', 'Wiedeń 12.IX.1683 | Chocim 11.XI.1673','Czaśniki 26.I.1564','Biały Kamień 25.IX.1604']
btype = ['land battle']*5
no = ['old slavic','hebrew','hebrew','greek','hebrew']
title = ['hetman wielki koronny','hetman wielki litewski','król','hetman wielki litewski','hetman wielki litewski']

ln = pd.Series(leadername)
ls = pd.Series(leadersurname)
b = pd.Series(battle)
bt = pd.Series(btype)
o = pd.Series(no)
t = pd.Series(title)

data = pd.DataFrame({'Leader Name': ln, 'Leader Surame': ls, 'Battle': b, 'Battle type': bt,
                     'Name origin': o, 'Title':t})
#print(data)
### a)

data['Battle'] = data['Battle'].str.split(' \| ')
data = data.explode('Battle')
data = data.reset_index(drop=True)

### b)

leaders = data[['Leader Name', 'Leader Surame', 'Name origin', 'Title']].drop_duplicates()
battle = data[['Battle', 'Battle type']].drop_duplicates()


### c)

leaders = leaders.reset_index()
battle = battle.reset_index()

# Łączenie ramek danych
l1 = leaders.copy()
l1 = l1.drop(['Name origin'], axis=1)
l2 = leaders.copy()
l2 = l2[['Leader Name', 'Leader Surame', 'Name origin']]

#print(l1)
#print(l2)

### d)

recreate_leaders = pd.merge(l1, l2, on=['Leader Name', 'Leader Surame'], how='left')

#print(recreate_leaders)
#print(leaders)
