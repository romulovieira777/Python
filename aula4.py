a = int(input('First quarter: '))
while a > 10:
    a = int(input('You typed it wrong. First quarter: '))
b = int(input('Second quarter: '))
while b > 10:
    b = int(input('You typed it wrong. Second quarter: '))
c = int(input('Third quarter: '))
while c > 10:
    c = int(input('You typed it wrong. Third quarter: '))
d = int(input('Fourth quarter: '))
while d > 10:
    d = int(input('You typed it wrong. Fourth quarter: '))
average = (a + b + c + d) / 4
print('Average: {}'.format(average))


# note = int(input('Enter a note: '))
# while note > 10:
#     note = int(input('Invalid note. Enter the correct grade: '))
# print(note)


# a = 0
# while a <= 10:
#     print(a)
#     a += 1


# a = int(input('Enter a value: '))
# for number in range(a + 1):
#     division = 0
#     for x in range(1, number + 1):
#         rest = number % x
#         if rest == 0:
#             division += 1
#     if division == 2:
#         print(number)


# a = int(input('Enter a value: '))
# division = 0
# for x in range(1, a + 1):
#     rest = a % 2
#     if rest == 0:
#         division += 1
# if division == 2:
#     print('Number {} is prime'.format(a))
# else:
#     print('Number {} is not prime'.format(a))
