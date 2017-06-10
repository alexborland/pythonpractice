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
import itertools

def get_input():
    string_of_numbers = input("> ")
    list_of_numbers = [int(i) for i in string_of_numbers.split(" ")]
    return list_of_numbers

def eval_single(x1, o1, x2):
    valid_operators = ["+", "-", "*", "/"]
    assert o1 in valid_operators
    if x2 == 0 and o1 == "/":
        return None
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
    

def eval_combination(operands, operators):
    valid_operators = ["+", "-", "*", "/"]
    for o in operators:
        assert o in set(valid_operators)
    assert len(operators) == len(operands) - 1
    result = operands[0]
    for i in range(len(operators)):
        result = eval_single(result, operators[i], operands[i + 1])
    return result

def mix_operators(size):
    operators = ["+", "-", "*", "/"]
    #return [["*", "+", "*", "+", "+"]]
    return itertools.product(operators, repeat = size)

def find_solution(operands, target):
    solution_results = []
    for i in itertools.permutations(operands):
        for j in mix_operators(len(operands) - 1):
            if eval_combination(i, j) == target:
                solution_results.append({"operands": i, "operators": j})
    return solution_results

numbers = get_input()
target = numbers.pop(-1)
operands = numbers

print(f"Target is {target}")
print(f"Operands are {operands}")

solutions = find_solution(operands, target)

for solution in solutions:
    print_string = str(solution["operands"][0])
    for i in range(len(solution["operators"])):
        print_string += " " + solution["operators"][i]
        print_string += " " + str(solution["operands"][i + 1])
    print_string += " = " + str(target)
    print(print_string)