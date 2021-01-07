import itertools 

def day14pt1(x):
    mem = {}
    mask = None
    for row in x:
        mem, mask = handleRow(row.strip(), mem, mask)
    return sum(mem.values())

def day14pt2(x):
    mem = {}
    mask = None
    for row in x:
        mem, mask = handleRowPt2(row.strip(), mem, mask)
    return sum(mem.values())  

def handleRowPt2(row, mem, mask):
    if 'mask' in row:
        mask = row.split(' ')[-1]
        return mem, mask
    else:
        init_val = int(row.split(' ')[-1])
        row = applyMaskPt2(row, mask)
        mem = updateMemPt2(row, mem, init_val)
        return mem, mask

def applyMaskPt2(row, mask):
    value = str('{0:036b}'.format(int(row[row.index('[')+1:row.index(']')])))
    for i in range(len(mask)):
        if mask[i] == '1':
            value = value[:i] + '1' + value[i+1:]
        if mask[i] == 'X':
            value = value[:i] + 'X' + value[i+1:]
    return getAllValues(value)

def getAllValues(value):
    indices = [i for i, x in enumerate(value) if x == "X"]
    data = []
    i = 0
    for j in indices:
        data.append([value[i:j]])
        data.append(['1','0'])
        i = j + 1
    data.append([value[i:]])
    return [int(''.join(i),2) for i in itertools.product(*data)]
    
def updateMemPt2(row, mem, init_val):
    for val in row:
        mem[val] = init_val
    return mem

def handleRow(row, mem, mask):
    if 'mask' in row:
        mask = row.split(' ')[-1]
        return mem, mask
    else:
        row = applyMask(row, mask)
        mem = updateMem(row, mem)
        return mem, mask

def updateMem(row, mem):
    key = int(row[row.index('[') + 1: row.index(']')])
    value = int(row.split(' ')[-1], 2)
    mem[key] = value
    return mem

def applyMask(row, mask):
    value = str('{0:036b}'.format(int(row.split(' ')[-1])))
    for i in range(len(mask)):
        if mask[i]!='X':
            value = value[:i] + mask[i] + value[i+1:]
    return row.replace(row.split(' ')[-1], value)

if __name__ == "__main__":
    text_file = open("day14/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day14pt1(x))
    print(day14pt2(x))
