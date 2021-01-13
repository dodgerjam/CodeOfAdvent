"""
Each move, the crab does the following actions:

The crab picks up the three cups that are immediately clockwise of the current cup. 
They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. 
If this would select one of the cups that was just picked up, the crab will keep subtracting one until 
it finds a cup that wasn't just picked up. 
If at any point in this process the value goes below the lowest value on any cup's label, 
it wraps around to the highest value on any cup's label instead.
The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. 
They keep the same order as when they were picked up.
The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
"""

def day23pt1(x):
    cups = [int(y) for y in x]
    
    current_cup = cups[0]
    current_index = 0
    for i in range(100):
        removed_cups = [cups[(current_index + i)%len(cups)] for i in [1,2,3]]
        destination_cup = current_cup - 1
        while destination_cup in removed_cups or destination_cup<1:
            destination_cup -= 1
            if destination_cup <1:
                destination_cup = max(cups)

        for cup in removed_cups:
            cups.pop(cups.index(cup))

        destination_index = cups.index(destination_cup)
        cups = cups[:destination_index+1] + removed_cups + cups[destination_index+1:]

        current_index = cups.index(current_cup)
        current_index += 1
        current_index %= len(cups)
        current_cup = cups[current_index]
    
    return getItemsAfterOne(cups)

def getItemsAfterOne(cups):
    index1 = cups.index(1)
    indexes = [i%len(cups) for i  in range(index1 +1, index1 + len(cups))]
    return ''.join([str(cups[i]) for i in indexes])


def day23pt2(x):
    cups = [int(y) for y in x]
    cups += [i for i in range(max(cups)+1, 10**6 + 1)]
    
    current_cup = cups[0]
    cups = dict(zip(cups, cups[1:] + cups[:1]))
    
    for i in range(10**7):
        pickups = []

        initpickup = current_cup
        for i in range(3):
            initpickup = cups[initpickup]
            pickups.append(initpickup)

        destination_cup = current_cup - 1
        while destination_cup in pickups or destination_cup<1:
            destination_cup -= 1
            if destination_cup <1:
                destination_cup = max(cups)

        cups[current_cup] = cups[pickups[-1]]
        cups[pickups[-1]] = cups[destination_cup]
        cups[destination_cup]= pickups[0]

        current_cup = cups[current_cup]
    return  cups[1] * cups[cups[1]]

def CupOrder(start, cups):
    order = []
    for i in range(len(cups)):
        order.append(start)
        start = cups[start]
    return order



if __name__ == "__main__":
    print(day23pt1("586439172"))
    print(day23pt2("586439172"))
