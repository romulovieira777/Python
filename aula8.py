calculator = {
    'soma': lambda a, b: a + b,
    'subtraction': lambda a, b: a - b,
    'multiplication': lambda a, b: a * b,
    'division': lambda a, b: a / b,
}
print(type(calculator))
soma = calculator['soma']
multiplication = calculator['multiplication']
subtraction = calculator['subtraction']
division = calculator['division']
print('The sum is: {}'.format(soma(10, 5)))
print('The multiplication is: {}'.format(multiplication(10, 5)))
print('The subtraction is: {}'.format(subtraction(10, 5)))
print('The division is: {}'.format(division(10, 5)))


# word_counter = lambda lista: [len(x) for x in lista]
#
# lista_animals = ['Dog', 'Cat', 'Elephant']
# print(word_counter(lista_animals))
#
# soma = lambda a, b: a + b
# subtraction = lambda a, b: a - b
# print(soma(5, 10))
# print(subtraction(10, 5))


# def word_counter(list_word):
#     counter = []
#     for x in list_word:
#         amount = len(x)
#         counter.append(amount)
#     return counter
#
# if __name__ == '__main__':
#     lista = ['Dog', 'Cat']
#     print(word_counter(lista))


# from aula7 import Television
#
# television = Television()
# print(television.on)
# television.power()
# print(television.on)
