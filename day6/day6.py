def day6pt1(x):
    total = 0
    for group in x.split('\n\n'):
        total += len([x for x in set(group) if x.isalpha()])
    return total

def day6pt2(x):
    all_answers = 0
    for group in x.split('\n\n'):
        for answer in [x for x in set(group) if x.isalpha()]:
            in_all = True
            for person in group.strip().split('\n'):
                if answer not in person:
                    in_all = False
                    break
            if in_all:
                all_answers += 1
    return all_answers


if __name__ == "__main__":
    with open("day6/input.txt", 'r') as file:
        data = file.read()
    print(day6pt1(data))
    print(day6pt2(data))
