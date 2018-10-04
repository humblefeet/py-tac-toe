#Variables
global player_X_moves
player_X_moves = []
global player_Y_moves
player_Y_moves = []
global total_moves
total_moves = []
global valid_moves
valid_moves = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
global moves
moves = {'a1':'','a2':'','a3':'','b1':'','b2':'','b3':'','c1':'','c2':'','c3':''}
global winning_combos
winning_combos = [
[moves['a1'],moves['a2'],moves['a3']],
[moves['b1'],moves['b2'],moves['b3']],
[moves['c1'],moves['c2'],moves['c3']],
[moves['a1'],moves['b1'],moves['c1']],
[moves['a2'],moves['b2'],moves['c2']],
[moves['a3'],moves['b3'],moves['c3']],
[moves['a1'],moves['b2'],moves['c3']],
[moves['a3'],moves['b2'],moves['c1']]]



#functions
def check_for_win():
    if len(total_moves) >= 9:
        for i in winning_combos:
            if player_X_moves not in i:
                print("Tie!")
                return
            elif player_Y_moves not in i:
                print("Tie!")
                return
    move_checker()

def move_checker():
    for x in winning_combos:
        if x[0] in player_X_moves and x[1] in player_X_moves and x[2] in player_X_moves:
            print("Player X Wins!")
        if x[0] in player_Y_moves and x[1] in player_Y_moves and x[2] in player_Y_moves:
            print("Player O Wins!")


#Player X move
def x_choice(): 
    choice = input("Player X move (example b3): ").lower()
    while choice in total_moves or choice not in valid_moves:
        choice = input("Bogus move! Try again...").lower()
    player_X_moves.append(choice)
    total_moves.append(choice)
    plug_letters(choice)
    print(player_X_moves)
    check_for_win()
    display_board()
    y_choice()


#Player Y move
def y_choice():
    choice = input("Player O move (example c2): ").lower()
    while choice in total_moves or choice not in valid_moves:
        choice = input("Bogus move! Try again...").lower()
    player_Y_moves.append(choice)
    total_moves.append(choice)
    plug_letters(choice)
    print(player_Y_moves)
    check_for_win()
    display_board()
    x_choice()


# adds letters to board
def plug_letters(t):
    if t in player_X_moves:
        moves[t] = 'X'
    elif t in player_Y_moves:
        moves[t] = "O"

#board
def display_board():
    print(f"""
        A   B   C

    1)   {moves['a1']} |   {moves['b1']} | {moves['c1']}
    -------------------
    2)   {moves['a2']} |   {moves['b2']} | {moves['c2']}
    -------------------
    3)   {moves['a3']} |   {moves['b3']} | {moves['c3']}
    
                                                    """)
    

#Calling of functions
print(""" 
        ----------------------
        Let's play Py-Pac-Poe!
        ----------------------""")
display_board()
x_choice()
y_choice()

