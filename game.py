#Variables
global game_over
game_over = False
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

##--Functions--##
#Brute force approach (Unfortunately)
def check_for_win(v):
    if len(total_moves) >= 9:
        for i in winning_combos:
            if player_X_moves not in i:
                print("Tie!")
                game_over = True
            elif player_Y_moves not in i:
                print("Tie!")
                game_over = True
    if moves['a1'] == v and moves['a2'] == v and moves['a3'] == v: 
        print(f"Player {v} winner!") 
        game_over = True
    if moves['b1'] == v and moves['b2'] == v and moves['b3'] == v: 
        print(f"Player {v} winner!") 
        game_over = True
    if moves['c1'] == v and moves['c2'] == v and moves['c3'] == v: 
        print(f"Player {v} winner!") 
        game_over = True
    if moves['a1'] == v and moves['b1'] == v and moves['c1'] == v: 
        print(f"Player {v} winner!") 
        game_over = True
    if moves['a2'] == v and moves['b2'] == v and moves['c2'] == v: 
        print(f"Player {v} winner!") 
        game_over = True
    if moves['a3'] == v and moves['b3'] == v and moves['c3'] == v: 
        print(f"Player {v} winner!") 
        game_over = True
    if moves['a1'] == v and moves['b2'] == v and moves['c3'] == v: 
        print(f"Player {v} winner!") 
        game_over = True
    if moves['c1'] == v and moves['b2'] == v and moves['a3'] == v: 
        print(f"Player {v} winner!") 
        game_over = True

#Player X move
def x_choice(): 
    choice = input("Player X move (example b3): ").lower()
    while choice in total_moves or choice not in valid_moves:
        choice = input("Bogus move! Try again...").lower()
    player_X_moves.append(choice)
    total_moves.append(choice)
    plug_letters(choice)
    check_for_win("X")
    display_board()
    while not game_over:
        y_choice()

#Player Y move
def y_choice():
    choice = input("Player O move (example c2): ").lower()
    while choice in total_moves or choice not in valid_moves:
        choice = input("Bogus move! Try again...").lower()
    player_Y_moves.append(choice)
    total_moves.append(choice)
    plug_letters(choice)
    check_for_win("O")
    display_board()
    while not game_over:
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

