
# Инверсия массива
# Циклический сдвиг влево и вправо
# Решето Эратосфена

A = [i for i in 'ваваоргеrghlcnvbfhtyr_u5rofofkqafsderxvzcsgfdrepoimfkv' ]
A.sort()
B = 'shemaeshemaeshemaeshemae'
f = ['a']
for i in B:
    f.append(i) if i in A and i not in f else None
# add new string
