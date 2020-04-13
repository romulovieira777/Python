conjunto = {1, 2, 3, 4, 5}
conjunto_2 = {5, 6, 7, 8}
conjunto_union = conjunto.union(conjunto_2)
print('Union: {}'.format(conjunto_union))
conjunto_intersection = conjunto.intersection(conjunto_2)
print('Intersection: {}'.format(conjunto_intersection))
conjunto_difference_1 = conjunto.difference(conjunto_2)
print('Difference between 1 and 2: {}'.format(conjunto_difference_1))
conjunto_difference_2 = conjunto_2.difference(conjunto)
print('Difference between 2 and 1: {}'.format(conjunto_difference_2))
conjunto_difference_symmetric = conjunto.symmetric_difference(conjunto_2)
print('Difference symmetric: {}'.format(conjunto_difference_symmetric))


# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4, 5}
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print('A is subset of B: {}'.format(conjunto_subset))
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print('B is a superset of A: {}'.format(conjunto_superset))
#
#
# lista = ['Dog', 'Dog', 'Cat', 'Cat', 'Elephant']
# print(lista)
# conjunto_animals = set(lista)
# print(conjunto_animals)
# lista_animals = list(conjunto_animals)
# print(lista_animals)


# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)
