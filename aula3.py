a = int(input('First quarter: '))
if a > 10:
    a = int(input('You typed it wrong. First quarter: '))
b = int(input('Second quarter: '))
if b > 10:
    b = int(input('You typed it wrong. Second quarter: '))
c = int(input('Third quarter: '))
if c > 10:
    c = int(input('You typed it wrong. Third quarter: '))
d = int(input('Fourth quarter: '))
if d > 10:
    d = int(input('You typed it wrong. Fourth quarter: '))
average = (a + b + c + d) / 4
print('Average: {}'.format(average))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Average: {}'.format(average))
# else:
#     print('Wrong note entered.')


# a = int(input('Enter a value: '))
# b = int(input('Enter a value: '))
# rest_a = a % 2
# rest_b = b % 2
# if rest_a == 0 or rest_b == 0:
#     print('An even number was entered.')
# else:
#     print('No even number has been entered.')


# a = int(input('First value: '))
# b = int(input('Second value: '))
# c = int(input('Third value: '))
# if a > b and a > c:
#     print('The highest value is: {}'.format(a))
# elif b > a and b > c:
#     print('The highest value is: {}'.format(b))
# else:
#     print('The highest value is: {}'.format(c))
# print('End of the program.')
