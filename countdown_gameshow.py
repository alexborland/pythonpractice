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
    

def eval_combination(x1, o1, x2, o2, x3, o3, x4, o4, x5, o5, x6):
    valid_operators = ["+", "-", "*", "/"]
    for o in [o1, o2, o3, o4, o5]:
        assert o in set(valid_operators)
    result = eval_single(x1, o1, x2)
    result = eval_single(result, o2, x3)
    result = eval_single(result, o3, x4)
    result = eval_single(result, o4, x5)
    result = eval_single(result, o5, x6)
    return result

def mix_operators():
    operators = ["+", "-", "*", "/"]
    result = []
    for i in operators:
        for j in operators:
            for k in operators:
                for m in operators:
                    for n in operators:
                        result.append([i, j, k, m, n])
    return result

def find_solution(x1, x2, x3, x4, x5, x6, target):
    operands = [x1, x2, x3, x4, x5, x6]
    for i in itertools.permutations(operands):
        for j in mix_operators():
            print(i[0], j[0], i[1], j[1], i[2], j[2], i[3], j[3], i[4], j[4], i[5])
            if eval_combination(i[0], j[0], i[1], j[1], i[2], j[2], i[3], j[3], i[4], j[4], i[5]) == target:
                return {"operands": i, "operators": j}

while True:
    try:
        numbers = get_input()
        operands = numbers[0:6]
        target = numbers[6]
        break
    except:
        print("Please enter exactly 7 numbers.")

print(f"Operands: {operands}")
print(f"Target: {target}")

solution = find_solution(operands[0], operands[1], operands[2], operands[3],
operands[4], operands[5], target)

out_string = ""
for i in range(5):
    out_string += str(solution['operands'][i])
    out_string += " "
    out_string += solution['operators'][i]
    out_string += " "
out_string += str(solution['operands'][5])
out_string += " = " + str(target)

print(out_string)
