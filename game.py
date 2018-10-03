#Variables
player_X_moves = []
player_Y_moves = []
total_moves = []
valid_moves = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
winning_combos = [['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3'],['a1','b2','c3'],['a3','b2','c1']]


moves = {'a1':' ','a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ','c2':' ','c3':' '}

print(f"""
   A   B   C

1) {moves['a1']}| {moves['b1']} |{moves['c1']}
-----------
2) {moves['a2']}| {moves['b2']} |{moves['c2']}
-----------
3) {moves['a3']}| {moves['b3']} |{moves['c3']}""")

#functions
def init_game():
    print(""" 
            ----------------------
            Let's play Py-Pac-Poe!
            ----------------------""")

init_game()

def check_for_win():
    if len(total_moves == 9):
        for i in winning_combos:
            if player_X_moves not in i:
                print("Tie!")
            elif player_Y_moves not in i:
                print("Tie!")
    for i in winning_combos:
        if len(player_X_moves) > 3 and player_X_moves in i:
            print("Player X wins the game!")
        elif len(player_Y_moves) > 3 and player_Y_moves in i:
            print("Player Y wins the game!")



def bogus_check(p):
    valid = True
    while valid:
        if p in player_X_moves or p in player_Y_moves:
            print("Bogus move! Try again...")
            valid = False
        elif p not in valid_moves:
            print("Bogus move! Try again...")
            valid = False


# #Player X move
def x_choice(): 
    choice = str(input("Player X move (example b3): "))
    bogus_check(choice)
    player_X_moves.append(choice)
    total_moves.append(choice)
    plug_letters(choice)
    
x_choice()

#Player Y move
def y_choice():
    choice = str(input("Player Y move (example c2): "))
    bogus_check(choice)
    player_Y_moves.append(choice)
    total_moves.append(choice)
    plug_letters(choice)

y_choice()

def plug_letters(x):
    if x in player_X_moves:
        moves[x] = 'X'
    elif x in player_Y_moves:
        moves[x] = "Y"
