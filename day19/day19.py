import itertools

def day19pt1(x, base = '0'):
    my_dict = {}
    for row in x[:x.index('\n')]:
        row = row.strip()
        pair = row.split(': ')
        key = pair[0]
        val = pair[1]
        if '|' in val:
            my_dict[key] = [[i for i in opt.split(' ')] for opt in val.split(' | ')]
        else:
            my_dict[key] = [[i if i.isnumeric() else i[1:-1] for i in val.split(' ')]]
    
    test_values = [x.strip() for x in x[x.index('\n')+1:]]

    alphabetical = [k for k,v in my_dict.items() if v[0][0].isalpha()]
    non_alphabetical = [k for k,v in my_dict.items() if v[0][0].isnumeric()]

    for key in alphabetical:
        my_dict[key] = [''.join(i) for i in my_dict[key]]

    while '0' not in alphabetical:
        for key in non_alphabetical:
            value = my_dict[key]
            if all([v in alphabetical for option in value for v in option]):
                non_alphabetical.remove(key)
                my_dict = transform(key, my_dict)
                alphabetical.append(key)
    
    return sum([i in my_dict['0'] for i in test_values])


def transform(key, my_dict):
    new_val = []
    for option in my_dict[key]:
        for option2 in itertools.product(*[my_dict[i] for i in option]):
            new_val.append(''.join(option2))
    my_dict[key] = new_val
    return my_dict

def day19pt2(x):
    my_dict = {}
    for row in x[:x.index('\n')]:
        row = row.strip()
        pair = row.split(': ')
        key = pair[0]
        val = pair[1]
        if '|' in val:
            my_dict[key] = [[i for i in opt.split(' ')] for opt in val.split(' | ')]
        else:
            my_dict[key] = [[i if i.isnumeric() else i[1:-1] for i in val.split(' ')]]
    
    test_values = [x.strip() for x in x[x.index('\n')+1:]]
    my_dict["8"] = [["42"], ["42", "8"]]
    my_dict["11"] = [["42", "31"], ["42", "11", "31"]]
    # my_dict["8"] = [["42" for i in range(n)] for n in range(1, 4)]
    # my_dict["11"] = [["42" for i in range(n)] + ["31" for i in range(n)] for n in range(1, 3)]
    alphabetical = [k for k,v in my_dict.items() if v[0][0].isalpha()]
    non_alphabetical = [k for k,v in my_dict.items() if v[0][0].isnumeric()]

    for key in alphabetical:
        my_dict[key] = [''.join(i) for i in my_dict[key]]

    alphabetical = [k for k,v in my_dict.items() if v[0][0].isalpha()]
    non_alphabetical = [k for k,v in my_dict.items() if v[0][0].isnumeric()]

    for key in alphabetical:
        my_dict[key] = [''.join(i) for i in my_dict[key]]

    while '42' not in alphabetical or '31' not in alphabetical:
        for key in non_alphabetical:
            value = my_dict[key]
            if all([v in alphabetical for option in value for v in option]):
                non_alphabetical.remove(key)
                my_dict = transform(key, my_dict)
                alphabetical.append(key)

    my_dict['42'] = list(set(my_dict['42']))
    my_dict['31'] = list(set(my_dict['31']))

    n = max([len(i) for i in my_dict['42']])
    
    count = 0
    for value in test_values:
        if rule0(value, my_dict['42'], my_dict['31'], n):
            count +=1
    
    return count

def rule0(value, dict42, dict31, n):
    if len(value)%n != 0:
        return False
    else:
        i = 0
        for i in range(n, len(value), n):
            if rule8(value[:i], dict42,n) and rule11(value[i:], dict42, dict31,n):
                return True
        return False

def rule8(value, dict42, n):
    for substring in [value[i:i+n] for i in range(0, len(value), n)]:
        if substring not in dict42:
            return False
    return True

def rule11(value, dict42, dict31, n):
    for substring in [value[i:i+n] for i in range(0, len(value)//2, n)]:
        if substring not in dict42:
            return False
    for substring in [value[i:i+n] for i in range(len(value)//2,len(value), n)]:
        if substring not in dict31:
            return False
    return True

if __name__ == "__main__":
    text_file = open("day19/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day19pt1(x))
    print(day19pt2(x))

