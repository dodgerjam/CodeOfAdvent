from functools import reduce

def day13pt1(x):
    earliest = int(x[0])
    buses = [int(bus) for bus in x[1].split(',') if bus != 'x']
    wait = [waitTime(earliest, frequency) for frequency in buses]
    return buses[wait.index(min(wait))] * min(wait)


def waitTime(earliest, frequency):
    return (1 + (earliest//frequency))*(frequency) - earliest

def day13pt2(x, min_guess = 0):
    # Chinese remainder theorem
    buses = {int(v):k for k,v in enumerate(x[1].split(',')) if v!='x'}
    M = reduce(lambda x,y: x*y, buses.keys())


    total = 0
    for bus in buses.keys():
        c = -buses[bus] % bus
        n = int(M / bus)
        nhat = pow(n, -1, bus)
        total += c * n * nhat
   
    return total % M

if __name__ == "__main__":
    text_file = open("day13/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day13pt1(x))
    print(day13pt2(x))
