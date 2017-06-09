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
def get_input():
    string_of_numbers = input("> ")
    list_of_numbers = [int(i) for i in string_of_numbers.split(" ")]
    return list_of_numbers

def eval_single(x1, o1, x2):
    valid_operators = ["+", "-", "*", "/"]
    assert o1 in valid_operators
    if o1 == "+":
        return x1 + x2
    elif o1 == "-":
        return x1 - x2
    elif o1 == "*":
        return x1 * x2
    elif o1 == "/":
        return float(x1 / x2)
    else:
        return None
    

def eval_combination(x1, o1, x2, o2, x3, o3, x4, o4, x5, o5, x6):
    valid_operators = ["+", "-", "*", "/"]
    assert set(x1, x2, x3, x4, x5, x6) in set(valid_operators)
    

while True:
    try:
        numbers = get_input()
        operands = numbers[0:5]
        target = numbers[6]
        break
    except:
        print("Please enter exactly 7 numbers.")

print("-: ", eval_single(operands[0],"-",operands[1]))
print("+: ", eval_single(operands[0],"+",operands[1]))
print("*: ", eval_single(operands[0],"*",operands[1]))
print("/: ", eval_single(operands[0],"/",operands[1]))