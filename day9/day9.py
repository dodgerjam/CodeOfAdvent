def day9pt1(x, prev=25):
    x = [int(i) for i in x]
    boolean = True
    i = 0
    while boolean:
        boolean = summable(x[prev+i], x[i:prev+i])
        i += 1
    return x[prev+i-1]


def summable(target, numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                return True
    return False

def summablelist(target, x):
    for i in range(len(x) - 1):
        for j in range(i, len(x)):
            if sum(x[i:j]) == target:
                return min(x[i:j]) + max(x[i:j])

def day9pt2(x, prev=25):
    x = [int(i) for i in x]
    target = day9pt1(x, prev=prev)
    return summablelist(target, x)



if __name__ == "__main__":
    text_file = open("day9/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day9pt1(x))
    print(day9pt2(x))
