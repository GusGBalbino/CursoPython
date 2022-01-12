# List Comprehension in Python

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
