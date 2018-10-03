#Variables
global player_X_moves
player_X_moves = []
global player_Y_moves
player_Y_moves = []
global total_moves
total_moves = []
global valid_moves
valid_moves = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
global winning_combos
winning_combos = [['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3'],['a1','b2','c3'],['a3','b2','c1']]
global moves
moves = {'a1':' ','a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ','c2':' ','c3':' '}


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
    for i in player_X_moves:
        for z in winning_combos:
            if i in z:
                print(z)
                

#Player X move
def x_choice(): 
    choice = str(input("Player X move (example b3): ")).lower()
    if choice not in total_moves and choice in valid_moves:
        player_X_moves.append(choice)
        total_moves.append(choice)
        plug_letters(choice)
        check_for_win()
        display_board()
        y_choice()
    else: 
        print("Bogus move! Try again...")
        return choice

#Player Y move
def y_choice():
    choice = str(input("Player O move (example c2): ")).lower()
    if choice not in total_moves and choice in valid_moves:        
        player_Y_moves.append(choice)
        total_moves.append(choice)
        plug_letters(choice)
        check_for_win()
        display_board()
        x_choice()
    else: 
        print("Bogus move! Try again...")
        return choice    

# adds letters to 
def plug_letters(t):
    if t in player_X_moves:
        moves[t] = 'X'
    elif t in player_Y_moves:
        moves[t] = "O"

def display_board():
    print(f"""
    A   B   C

    1) {moves['a1']}| {moves['b1']} |{moves['c1']}
    -----------
    2) {moves['a2']}| {moves['b2']} |{moves['c2']}
    -----------
    3) {moves['a3']}| {moves['b3']} |{moves['c3']}""")
    

print(""" 
        ----------------------
        Let's play Py-Pac-Poe!
        ----------------------""")
display_board()
x_choice()
y_choice()

print(winning_combos[8])