def random_stuff(number_one, number_two):
    easy_square = number_one * number_one
    first_cube = number_two * number_two * number_two
    return easy_square, first_cube

number = input("Pick a number:")
number = int(number)
second_number = input("Pick another one:")
second_number = int(second_number)
easy, first = random_stuff(number, second_number)
print(f"{number} squared is {easy} and {second_number} cubed is {first}")

