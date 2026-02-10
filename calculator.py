def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print(art.logo)

result = ''
is_stop = False
continue_calc = 'y'

def perform_calculation():
    global result
    global continue_calc

    while continue_calc == 'y' and not is_stop:
        expression = input('Please enter your expression: ')

        expression_list = expression.split(' ')

        current_operator = ''

        for i in range(0, len(expression_list)):

            if i == 0 and type(result) == str:
                result = float(expression_list[0])
            else:
                if not expression_list[i].isdigit():
                    current_operator = expression_list[i]
                    continue
                else:
                    if current_operator == '+':
                        result = add(result,float(expression_list[i]))
                    elif current_operator == '-':
                        result = sub(result,float(expression_list[i]))
                    elif current_operator == '*':
                        result = mul(result,float(expression_list[i]))
                    elif current_operator == '/':
                        result = div(result,float(expression_list[i]))

        print(f'Result: {result}')
        continue_calc = input('Continue calc? (y/n/s): ')
        if continue_calc == 'n':
            result = ''
            continue_calc = input('New calc? (y/n)')
        elif continue_calc == 's':
            return

perform_calculation()