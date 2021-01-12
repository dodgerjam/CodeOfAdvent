import copy

def day22pt1(x):
    x = [y.strip() for y in x]
    player1 = [int(y) for y in x[x.index('Player 1:')+1:x.index('')]]
    player2 = [int(y) for y in x[x.index('Player 2:')+1:]]

    while len(player1)!=0 and len(player2)!=0:
        player1, player2 = playGame(player1, player2)
    
    endgame = (player1 + player2)[::-1]
    score = 0
    for count, card in enumerate(endgame, start=1):
        score += count * card
    return score

def playGame(player1, player2):
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    if p2 > p1:
        player2.append(p2)
        player2.append(p1)
    return player1, player2

def day22pt2(x):
    
    x = [y.strip() for y in x]
    player1 = [int(y) for y in x[x.index('Player 1:')+1:x.index('')]]
    player2 = [int(y) for y in x[x.index('Player 2:')+1:]]
    winner, endgame = playRecursiveGame(player1, player2, previous_rounds = [])
    score = 0
    for count, card in enumerate(endgame[::-1], start=1):
        score += count * card
    return score

def playRecursiveGame(player1, player2, previous_rounds = []):
    nround = 0
    while len(player1)!=0 and len(player2)!=0:
        nround += 1
        # print(f"-- ROUND{nround} --")
        # print("Player 1's Deck: ", player1)
        # print("Player 2's Deck: ", player2)
        round_name = '_'.join([str(i) for i in player1]) + '/' + '_'.join([str(i) for i in player2])
        if round_name in previous_rounds:
            # print(round_name)
            # print(previous_rounds)
            # print("Player 1 Wins by previous round!")
            return "1", player1
        previous_rounds.append(round_name)

        p1 = player1.pop(0)
        p2 = player2.pop(0)
        # if both players have at least as many cards in their own decks as the number on the card they just dealt, 
        # the winner of the round is determined by recursing into a sub-game of Recursive Combat.
        if len(player1) >= p1 and len(player2) >= p2:
            # print("\nPlaying New Game")
            recursiveGameWinner, result = playRecursiveGame(copy.deepcopy(player1[:p1]), copy.deepcopy(player2[:p2]), previous_rounds=[])
            if recursiveGameWinner == "1":
                player1.append(p1)
                player1.append(p2)
            if recursiveGameWinner == "2":
                player2.append(p2)
                player2.append(p1)
        else:
            if p1 > p2:
                player1.append(p1)
                player1.append(p2)
            if p2 > p1:
                player2.append(p2)
                player2.append(p1)
    
    if len(player1) == 0:
        # print("Player 2 wins!")
        return "2", player2
    else:
        # print("Player 1 wins!")
        return "1", player1
   
if __name__ == "__main__":
    text_file = open("day22/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day22pt1(x))
    print(day22pt2(x))