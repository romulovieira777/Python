class Television:
    def __init__(self):
        self.on = False
        self.channel = 5

    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def increase_channel(self):
        if self.on:
            self.channel += 1

    def decrease_channel(self):
        if self.on:
            self.channel -= 1
if __name__ == '__main__':
    television = Television()
    print('Television is on: {}'.format(television.on))
    television.power()
    print('Television is on: {}'.format(television.on))
    television.power()
    print('Television is on: {}'.format(television.on))
    print('Channel: {}'.format(television.channel))
    television.power()
    print('Television is on: {}'.format(television.on))
    television.increase_channel()
    television.increase_channel()
    print('Channel: {}'.format(television.channel))
    television.decrease_channel()
    print('Channel: {}'.format(television.channel))


# class Calculator:
#     def __init__(self):
#         pass
#
#     def soma(self, value_a, value_b):
#         return value_a + value_b
#
#     def subtraction(self, value_a, value_b):
#         return value_a - value_b
#
#     def multiplication(self, value_a, value_b):
#         return value_a * value_b
#
#     def division(self, value_a, value_b):
#         return value_a / value_b
#
# calculator = Calculator()
# print(calculator.soma(10, 2))
# print(calculator.subtraction(5, 3))
# print(calculator.division(100, 2))
# print(calculator.multiplication(10, 5))


# class Calculator:
#     def __init__(self, number_1, number_2):
#         self.value_a = number_1
#         self.value_b = number_2
#
#     def soma(self):
#         return self.value_a + self.value_b
#
#     def subtraction(self):
#         return self.value_a - self.value_b
#
#     def multiplication(self):
#         return self.value_a * self.value_b
#
#     def division(self):
#         return self.value_a / self.value_b
#
# calculator = Calculator(10 , 2)
# print(calculator.value_a)
# print(calculator.soma())
# print(calculator.subtraction())
# print(calculator.division())
# print(calculator.multiplication())
