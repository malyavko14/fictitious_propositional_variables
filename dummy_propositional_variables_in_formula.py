def variables_in_formula(formula):
    variables = []
    count_of_numbers = 0
    formula = formula.upper()
    for i in range(65, 91):
        symbol = chr(i)
        if formula.count(symbol) > 0:
            count_of_numbers += 1
            variables.append(symbol)
    return variables


def list_of_numbers(number: int):
    binary_list = []
    if number == 1:
        return [[0], [1]]
    if number == 2:
        return [[0, 0], [0, 1], [1, 0], [1, 1]]
    for i in range(number ** 2 - 1):
        tmp = []
        while i >= 1:
            tmp.insert(0, i % 2)
            i = i // 2
        while len(tmp) < number:
            tmp.insert(0, 0)
        binary_list.append(tmp)
    return binary_list


def implication(a, b):
    if a == 1 and b == 0:
        return 0
    else:
        return 1


def equivalence(a, b):
    if a == b:
        return 1
    else:
        return 0


def search_for_extreme_brackets(formula):
    left_parenthesis = 0
    right_parenthesis = 0
    for j in range(len(formula)):
        if formula[j] == '(':
            left_parenthesis = j
    for j in range(left_parenthesis, len(formula)):
        if formula[j] == ')':
            right_parenthesis = j
            break
    if right_parenthesis == len(formula) - 1 and left_parenthesis == 0:
        subnormal = formula
    elif right_parenthesis == len(formula) - 1:
        subnormal = formula[left_parenthesis:]
    elif left_parenthesis == 0:
        subnormal = formula[:right_parenthesis + 1]
    else:
        subnormal = formula[left_parenthesis:right_parenthesis + 1]
    subnormal = subnormal.replace(' ', '')
    return subnormal


def casting_string_to_code(subnormal, variable, value, variables):
    if subnormal.count('->!'):
        subnormal = f'implication({subnormal[1]},{subnormal[-3:-1]})'
    elif subnormal.count('->') and subnormal.count('!'):
        subnormal = f'implication({subnormal[1:3]},{subnormal[-2]})'
    elif subnormal.count('->'):
        subnormal = f'implication({subnormal[1]},{subnormal[-2]})'
    if subnormal.count('~!'):
        subnormal = f'equivalence({subnormal[1]},{subnormal[-3:-1]})'
    elif subnormal.count('~') and subnormal.count('!'):
        subnormal = f'equivalence({subnormal[1:3]},{subnormal[-2]})'
    elif subnormal.count('~'):
        subnormal = f'equivalence({subnormal[1]},{subnormal[-2]})'
    subnormal = subnormal.replace('*', ' and ')
    subnormal = subnormal.replace('+', ' or ')
    subnormal = subnormal.replace(variable, f'{value}')
    subnormal = subnormal.replace("!", 'not ')

    k = 0
    for j in variables:
        subnormal = subnormal.replace(f"{j}", f"binary_numbers[i][{k}]")
        k += 1
    return subnormal


def remove_brackets(formula):
    formula = formula[1:-1]
    for i in range(len(formula) - formula.count('!') * 2):
        if formula[i] == '!':
            formula = formula[:i - 1] + formula[i:]
            tmp = i
            while formula[tmp] != ')':
                tmp += 1
            formula = formula[:tmp] + formula[tmp + 1:]
    return formula


def new_formula(formula, variable, value):
    truth_table = ''
    variables = variables_in_formula(formula)
    variables.remove(variable)
    formula = formula
    formula = formula.replace('/\\', '*')
    formula = formula.replace('\\/', '+')
    tmp = formula
    binary_numbers = list_of_numbers(len(variables))

    if len(binary_numbers) == 0:
        subnormal = '(' + formula + ')'
        subnormal = casting_string_to_code(subnormal, variable, value, variables)
        if eval(subnormal):
            truth_table += '1'
        else:
            truth_table += '0'
    else:
        for i in range(len(binary_numbers)):
            formula = tmp
            while formula.count('(') > 0:
                subnormal = search_for_extreme_brackets(formula)
                try:
                    res = eval(casting_string_to_code(subnormal, variable, value, variables))
                except SyntaxError:
                    return 0
                if res == 1:
                    formula = formula.replace(subnormal, '1')
                else:
                    formula = formula.replace(subnormal, '0')
            subnormal = '(' + formula + ')'
            try:
                if eval(casting_string_to_code(subnormal, variable, value, variables)):
                    truth_table += '1'
                else:
                    truth_table += '0'
            except SyntaxError:
                return 0
    return truth_table


def result(formula):
    formula = remove_brackets(formula)
    fictive_variables = []
    variables = variables_in_formula(formula)
    for i in variables:
        if new_formula(formula, f'{i}', 0) == 0:
            return 'Check that the formula is correct'
        if new_formula(formula, f'{i}', 0) == new_formula(formula, f'{i}', 1):
            fictive_variables.append(i)
    if len(fictive_variables) == 0:
        return 'There are no fictitious propositional variables in this formula'
    else:
        return f'Fictitious propositional variables: {str(fictive_variables)}'
