import networkx

def day10pt1(x):
    x = sorted([int(i) for i in x] + [0])
    diff1 = 0
    diff3 = 0
    for i in range(len(x)-1):
        if x[i+1] - x[i] == 1:
            diff1 += 1
        if x[i+1] - x[i] == 3:
            diff3 += 1
    return diff1 * (diff3 + 1)
    
def day10pt2(x):
    x = sorted([int(i) for i in x] + [0])[::-1]
    my_dict = {}
    my_dict[max(x)] = 1
    for i in x[1:]:
        possible_values = [j for j in x if j>i and j<=i+3]
        score = 0
        for j in possible_values:
            score += my_dict[j]
        my_dict[i] = score
    return my_dict[0]
    
def rEcUrSiOn(num, my_dict, max_val):
    if num == max_val:
        return 1
    else:
        score = 0
        for num in my_dict[num]:
            score += rEcUrSiOn(num, my_dict, max_val)
        return score

if __name__ == "__main__":
    text_file = open("day10/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day10pt1(x))
    print(day10pt2(x))
