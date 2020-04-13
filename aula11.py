# lista = [1, 10]
#
# try:
#     archive = open('test.txt', 'r')
#     text = archive.read()
#     division = 10 / 1
#     number = lista[1]
#     archive.close()
#
# except ZeroDivisionError:
#     print('Unable to divide by 0')
# except ArithmeticError:
#     print('There was an error performing an arithmetic operation')
# except IndexError:
#     print('Error accessing invalid list index')
# except Exception as ex:
#     print('Unknown error. Error: {}'.format(ex))
# else:
#     print('Runs when no exception occurs')
# finally:
#     print('Always perform')
#     print('Closing archive')
#     # archive.close()

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Enter a score from 0 to 10: '))
        print(x)
        if x > 10:
            raise InputError('Note cannot be greater than 10')
        elif x < 0:
            raise InputError('Note cannot be less than 0')
        break
    except ValueError:
        print('Invalid value. You must enter only numbers.')
    except InputError as ex:
        print(ex)
