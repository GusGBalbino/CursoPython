# List Comprehension in Python
'''
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ex1 = [var for var in l1]

ex2 = [var * 2 for var in l1]
ex3 = [(var, var2) for var in l1 for var2 in range(3)]

l2 = ['Gus', 'Gomes']
ex4 = [var.replace('G', '@').upper() for var in l2]


l3 = list(range(100))
ex6 = [var for var in l3 if var % 3 == 0 if var % 8 == 0]

ex7 = [var if var % 3 == 0 and var % 8 == 0 else 0 for var in l3]

print(ex7)
'''

'''
# Dictionary Comprehension in Python
lista4 = [('key', 'value'), ('key2', 'value2')]

d1 = {x: y for x, y in lista4}
print(d1)

d2 = {f'key_{x}': x**2 for x in range(6)}
print(d2)
'''

'''
# Zip and Zip_longest
from itertools import zip_longest, count

ind = count()

states = ['DF','MG','SP','BA','MT', 'PB']

cities = ['Brasília', 'Belo Horizonte', 'São Paulo', 'Salvador']

city_state = zip(ind,states, cities)
#city_state = zip_longest(states, cities, fillvalue= 'City')

for ind,states, cities in city_state:
    print(f'{ind} - {cities} - {states}')
'''
# Group By
from itertools import groupby

students = [
    {'Name':'Gus', 'Grade':'A'},
    {'Name':'Yas', 'Grade':'A'},
    {'Name':'Lopes', 'Grade':'B'},
    {'Name':'Marcelo', 'Grade':'B'},
    {'Name':'Bea', 'Grade':'C'},
    {'Name':'Julian', 'Grade':'C'},
    {'Name':'Maria', 'Grade':'D'},
    {'Name':'Gabi', 'Grade':'D'},
    {'Name':'Malu', 'Grade':'F'},
    {'Name':'Daniel', 'Grade':'F'},
]

order = lambda item: item['Grade']
students.sort(key=order)
students_groups = groupby(students, order)

for grouping, grouping_value in students_groups:
    print(f'Grouping {grouping} : ')
    for students in grouping_value:
        print(students)
    print()
