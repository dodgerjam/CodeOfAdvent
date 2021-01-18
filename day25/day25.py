def day25pt1(x):
    card_pub = int(x[0])
    door_pub = int(x[1])

    card = 7
    door = 7
    
    card_loop_size = 1
    while card != card_pub:
        card = handshake(card)
        card_loop_size +=1
    
    door_loop_size = 1
    while door != door_pub:
        door = handshake(door)
        door_loop_size +=1
    

    for i in range(card_loop_size-1):
        door = handshake(door, subject_number=door_pub)
    
    for i in range(door_loop_size-1):
        card = handshake(card, subject_number=card_pub)

    assert card == door

    return card

def handshake(x, subject_number=7):
    x *= subject_number
    x %= 20201227
    return x

if __name__ == "__main__":
    text_file = open("day25/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day25pt1(x))
