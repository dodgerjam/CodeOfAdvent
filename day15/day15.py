def day15pt1(start, n_number = 2020):
    for i in range(len(start), n_number):
        last_number = start[-1]
        if last_number in start[:-1]:
            new_number = start[:-1][::-1].index(last_number) + 1
        else:
            new_number = 0
        start.append(new_number)
    return start[-1]

def day15pt2(start, n_number = 30000000):
    # my dict is going to be the index of each element
    my_dict = {i: start.index(i) for i in start}
    last_number = start[-1]
    for i in range(len(start), n_number):
        if last_number in my_dict.keys():
            new_number = i - my_dict[last_number] - 1
        else:
            new_number = 0
        my_dict[last_number] = i - 1
        last_number = new_number
       
    return last_number

if __name__ == "__main__":
    #start = [14,8,16,0,1,17]
    print(day15pt1([14,8,16,0,1,17]))
    print(day15pt2([14,8,16,0,1,17]))

