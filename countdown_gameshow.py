def get_input():
    string_of_numbers = input("> ")
    list_of_numbers = [int(i) for i in string_of_numbers.split(" ")]
    return list_of_numbers

# we need to take an input of 7 numbers
# first six are operands, last one is the target
# we want to find some combination of operators such that:
# x1 ? x2 ? x3 ? x4 ? x5 ? x6 = x7
# where ? is +, -, *, or / and evaluated left-to-right
# it appears I'm allowed to reorder the input

# This is like the game "24" from elem school

# challenge input:
# 25 100 9 7 3 7 881 -> 7 * 3 + 100 * 7 + 25 + 9 = 881
# 6 75 3 25 50 100 952 -> 100 + 6 * 3 * 75 - 50 / 25 = 952
