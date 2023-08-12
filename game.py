# terminal clear command 
# def clear(): # Author Avideb

    
# clear the game screen before starting the game Author -> Avideb
# clear()

def draw(board):
    # clear()
    print(
        '''
  %s  │  %s  │  %s
──────┼──────┼──────
  %s  │  %s  │  %s
──────┼──────┼──────
  %s  │  %s  │  %s
''' % (
        board[1], board[2], board[3],
        board[4], board[5], board[6],
        board[7], board[8], board[9],
    ))



def who_is_the_winner(board, players):
    T_wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    for n in T_wins:

        if (board[n[0]] == players[0][1] and board[n[1]] == players[0][1] and board[n[2]] == players[0][1] ):
             return players[0][0]

        elif (board[n[0]] == players[1][1] and board[n[1]] == players[1][1] and board[n[2]] == players[1][1]):
            return players[1][0]

    return -1


# =======( game data )=======

board = [ 'tic tac toe',

    ' 1', ' 2', ' 3',
    ' 4', ' 5', ' 6',
    ' 7', ' 8', ' 9',
]

# default configuration for symbol, Author -> Avideb
sym1 = "🟢"
sym2 = "❌"
# player's name input
# player 1 has rights to chose symbol

pl1 = input("Enter Player1's Name : ")
opt = input(f"Choose your symbol (1.{sym1} or 2.{sym2}) : ")
if (int(opt) == 2):
    sym2, sym1 = sym1, sym2
pl2 = input ("Enter Player2's Name : ")

p1 = [ pl1, sym1]
p2 = [ pl2, sym2 ]

# ===========================


# game logo
print(board[0])

# game starts
draw(board)

turn = 1

while turn <= 9:
    if turn & 1:
        player = p1
    else:
        player = p2
    # player = p1 if(turn & 1) else p2 # Author -> Avideb

    name, spirit = player

    pos = input(f" {name}'s turn {spirit} > ")

    pos = int(pos) # exception may occur here

    if 1 <= pos <= 9 and board[pos] != p1[1] and board[pos] != p2[1]:
        board[pos] = spirit

        turn += 1

        if turn >= 5:
            winner = who_is_the_winner(board, [p1, p2])
            if(winner != -1):
                draw(board)
                break

    draw(board)

if(winner != -1):
    print(winner,"won")
else :
    print("its a draw")

    


