def day21pt1(x):

    allergens = set()
    ingredients = set()
    for row in x:
        for a in getAllergens(row):
            allergens.add(a)
        for i in getIngredients(row):
            ingredients.add(i)
    my_dict = {a:{} for a in allergens}
    for i in ingredients:
        for a in allergens:
            my_dict[a][i] = 0

    for count, row in enumerate(x):
        alls = getAllergens(row)
        ings = getIngredients(row)

        for i in ings:
            for a in alls:
                my_dict[a][i] += 1
    inv_dict = {}
    while len(inv_dict.keys()) != len(allergens):
        for key, dict_value in my_dict.items():
            max_vals = [i for i in dict_value.values() if i == max(dict_value.values())]
            if len(max_vals) == 1:
                max_key = max(dict_value, key=dict_value.get)
                inv_dict[max_key] = key
                my_dict.pop(key)
                # remove 
                for key1, dict_value1 in my_dict.items():
                    if max_key in dict_value1.keys():
                        dict_value1.pop(max_key)
                break
    
    absent = [i for i in ingredients if i not in inv_dict.keys()]
    count = 0
    for row in x:
        count+= len(set(absent).intersection(set(getIngredients(row))))
    return count


def day21pt2(x):

    allergens = set()
    ingredients = set()
    for row in x:
        for a in getAllergens(row):
            allergens.add(a)
        for i in getIngredients(row):
            ingredients.add(i)
    my_dict = {a:{} for a in allergens}
    for i in ingredients:
        for a in allergens:
            my_dict[a][i] = 0

    for count, row in enumerate(x):
        alls = getAllergens(row)
        ings = getIngredients(row)

        for i in ings:
            for a in alls:
                my_dict[a][i] += 1
    inv_dict = {}
    while len(inv_dict.keys()) != len(allergens):
        for key, dict_value in my_dict.items():
            max_vals = [i for i in dict_value.values() if i == max(dict_value.values())]
            if len(max_vals) == 1:
                max_key = max(dict_value, key=dict_value.get)
                inv_dict[max_key] = key
                my_dict.pop(key)
                # remove 
                for key1, dict_value1 in my_dict.items():
                    if max_key in dict_value1.keys():
                        dict_value1.pop(max_key)
                break
    
    
    return ','.join(sorted(inv_dict, key=inv_dict.get))
                  
def getIngredients(x):
    return x[:x.index(' (')].split(' ')

def getAllergens(x):
    return x[x.index("(contains ")+10: x.index(")")].split(', ')

if __name__ == "__main__":
    text_file = open("day21/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day21pt1(x))
    print(day21pt2(x))