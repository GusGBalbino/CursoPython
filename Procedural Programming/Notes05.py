# List Comprehension in Python

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ex1 = [var for var in l1]

ex2 = [var * 2 for var in l1]
ex3 = [(var, var2) for var in l1 for var2 in range(3)]

l2 = ['Gus', 'Gomes']
ex4 = [var.replace('G', '@').upper() for var in l2]

print(ex4)
