import re

def day18pt1(x):
    results = [int(calculateL2R(''.join([i for i in calc.strip()]))) for calc in x]
    return sum(results)

def day18pt2(x):
    results = [int(calculateAddFirst(''.join([i for i in calc.strip()]))) for calc in x]
    return sum(results)

def calculateAddFirst(calculation):
    while '(' in calculation:
        start_index = calculation.index('(')
        final_index = start_index +1
        count = 1
        while count != 0:
            if calculation[final_index] == '(':
                count += 1
            if calculation[final_index] == ')':
                count -= 1
            final_index += 1
        calculation = calculation[:start_index] + calculateAddFirst(calculation[start_index+1:final_index-1]) + calculation[final_index:]

    while '+' in calculation:
        split = re.split('(\d+)', calculation)[1:-1]
        index = split.index(' + ')
        new_val = str(eval(''.join(split[index-1:index+2])))
        calculation = calculation.replace(' '.join(calculation.split(' ')[index-1:index+2]), new_val, 1)
    
    return str(eval(calculation))

def calculateL2R(calculation):
    while '(' in calculation:
        start_index = calculation.index('(')
        final_index = start_index +1
        count = 1
        while count != 0:
            if calculation[final_index] == '(':
                count += 1
            if calculation[final_index] == ')':
                count -= 1
            final_index += 1
        calculation = calculation[:start_index] + calculateL2R(calculation[start_index+1:final_index-1]) + calculation[final_index:]

    while not calculation.isnumeric():
        l1 = str(eval(''.join(re.split('(\d+)', calculation)[1:-1][:3])))
        calculation = calculation.replace(' '.join(calculation.split(' ')[:3]), l1, 1)
    
    return calculation





if __name__ == "__main__":
    text_file = open("day18/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day18pt1(x))
    print(day18pt2(x))
