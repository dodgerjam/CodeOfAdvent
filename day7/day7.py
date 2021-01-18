def day7pt1(x):
    my_dict = createDict(x)
    return len(list(set(getAllGold('shiny gold bag', my_dict=my_dict))))

def day7pt2(x):
    my_dict = createDictPt2(x)
    return getNumOfBags('shiny gold bag', my_dict) - 1

def getAllGold(bag, my_dict, my_list = [],):
    if bag not in my_dict.keys():
        return my_list
    if my_dict[bag] == []:
        return my_list
    for bag in my_dict[bag]:
        my_list.append(bag)
        my_list = getAllGold(bag, my_dict, my_list = my_list)
    return my_list


def cleanUpBag(bag):
    bag = bag.strip()
    if bag[-1]=='s':
        return bag[:-1]
    else:
        return bag

def createDict(x):
    my_dict = {}
    for line in x:
        in_out = line.split(' contain ')
        contains = in_out[1].split(', ')

        for bag_type in contains:
            bag_type = ''.join([x for x in bag_type if x.isalpha() or x == ' '])
            if cleanUpBag(bag_type) not in my_dict.keys():
                my_dict[cleanUpBag(bag_type)] = [cleanUpBag(in_out[0])]
            else:
                my_dict[cleanUpBag(bag_type)].append(cleanUpBag(in_out[0]))
    return my_dict

def createDictPt2(x):
    my_dict = {}
    for line in x:
        in_out = line.split(' contain ')
        contains = in_out[1].split(', ')

        for bag_type in contains:
            n_bags = bag_type.split(' ')[0]
            if n_bags == 'no':
                n_bags = 0
            else:
                n_bags = int(n_bags)
            bag_type = ''.join([x for x in bag_type if x.isalpha() or x == ' '])
            if cleanUpBag(in_out[0]) not in my_dict.keys():
                my_dict[cleanUpBag(in_out[0])] = [(cleanUpBag(bag_type), n_bags)]
            else:
                my_dict[cleanUpBag(in_out[0])].append((cleanUpBag(bag_type), n_bags))
    return my_dict

def getNumOfBags(bag, my_dict):
    if bag not in my_dict.keys():
        return 1
    if my_dict[bag] == []:
        return 1
    total = 1
    for b in my_dict[bag]:
        b, n_bags = b
        total += n_bags * getNumOfBags(b, my_dict)
    return total

if __name__ == "__main__":
    text_file = open("day7/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day7pt1(x))
    print(day7pt2(x))
    