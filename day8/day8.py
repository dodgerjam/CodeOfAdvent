import copy

def day8pt1(x):
    accumulator = 0
    i = 0
    used_rows = []
    max_rows = len(x)

    while i not in used_rows:
        used_rows.append(i)
        operation, argument = x[i].split(' ')
        if operation == 'nop':
            i += 1
            i %= max_rows
        if operation == 'acc':
            i += 1
            i %= max_rows
            accumulator += getArgument(argument)
        if operation == 'jmp':
            i += getArgument(argument)
            i %= max_rows
    return accumulator

def findPerms(x):
    accumulator = 0
    i = 0
    used_rows = []
    perms = []
    max_rows = len(x)

    while i not in used_rows:
        used_rows.append(i)
        operation, argument = x[i].split(' ')
        if operation == 'nop':
            perms.append(i)
            i += 1
            i %= max_rows
        if operation == 'acc':
            i += 1
            i %= max_rows
            accumulator += getArgument(argument)
        if operation == 'jmp':
            perms.append(i)
            i += getArgument(argument)
            i %= max_rows

    return perms

def day8pt1a(x):
    accumulator = 0
    i = 0
    used_rows = []
    max_rows = len(x)

    while i not in used_rows:
        used_rows.append(i)
        operation, argument = x[i].split(' ')
        if operation == 'nop':
            i += 1
            i %= max_rows
        if operation == 'acc':
            i += 1
            i %= max_rows
            accumulator += getArgument(argument)
        if operation == 'jmp':
            i += getArgument(argument)
            i %= max_rows
    return accumulator, used_rows[-1] == max_rows-1


def permutation(x, i):
    new_x = [i for i in x]
    if new_x[i][:3] == 'nop':
        new_x[i] = new_x[i].replace('nop', 'jmp')
        return new_x
    if new_x[i][:3] == 'jmp':
        new_x[i] = new_x[i].replace('jmp', 'nop')
        return new_x



def day8pt2(x):
    perms = findPerms(x)
    for perm in perms:
        new_x = permutation(x, perm)
        accumulator, boolean = day8pt1a(new_x)
        if boolean:
            return accumulator



def getArgument(argument):
    if argument[0] == '+':
        return int(argument[1:])  
    if argument[0] == '-':
        return -int(argument[1:])  


if __name__ == "__main__":
    text_file = open("day8/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day8pt1(x))
    print(day8pt2(x))
    