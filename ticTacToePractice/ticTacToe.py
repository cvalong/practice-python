# a Tic Tac Toe game made with a list of lists

# repetitive code? use a function or loops etc. to reduce error and such
# including some args and default args for the fxn that was made, what if we wanted to just display the board, etc.
import itertools

def game_board(game_map, player=0, row=0, column=0, just_display=False):
        # added a return for the game_map
        try:
                if game_map[row][column] != 0:
                        print("This position is occupied! Choose another!")
                        return game_map, False
                
                #for a bigger game of tic tac toe
                s = " "
                for i in range (len(game_map)):
                        s += "  "+str(i)
                print(s)

                # # or this version: 
                # print("   "+"  ".join([str(i) for i in range(len(game_map))]))

                if not just_display:
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print (count, row)
                
                return game_map, True
        
        # added some level of error handling
        except IndexError as e:
                print("Error: make sure you input rows/column as 0 1 or 2?", e)
                return game_map, False
        
        except Exception as e:
                print("something went very wrong!", e)
                return game_map, False

#condensed win fxns into a single fxn and added return values
def win(current_game):
        
        #added return values to this fxn as well
        def all_same(list):
                if list.count(list[0]) == len(list) and list[0] != 0:
                        return True
                else:
                        return False
                #should probably try to pull in the printed "win" to this helper fxn


        # horizontal
        for row in current_game:
                if all_same(row):
                        print(f"Player {row[0]} is the winner horizontally!")
                        return True

        # vertical
        for col in range(len(current_game)):
                check = []

                for row in current_game:
                        check.append(row[col])

                if all_same(check):
                        print(f"Player {check[0]} is the winner vertically (|)!")
                        return True

        # one diagonal
        diags = []
        for index in range(len(current_game)):
                diags.append(current_game[index][index])
        if all_same(diags):
                print(f"Player {diags[0]} is the winner diagonally (\\)!")
                return True

        # the other diagonal
        diags = []
        for col, row in enumerate(reversed(range(len(current_game)))):
                diags.append(game[row][col])        
        if all_same(diags):
                print(f"Player {diags[0]} is the winner diagonally (/)!")
                return True
        
        return False

#input for the game
play = True
players = [1, 2]
while play:
        
        # dynamic size game of tic tac toe
        game_size = int(input("What size game of tic tac toe? "))
        game = [[0 for i in range(game_size)] for i in range(game_size)]

        game_won = False
        game, _ = game_board(game, just_display=True)

        #itertools to cycle between player 1 and 2
        player_choice = itertools.cycle([1, 2])
        while not game_won:
                current_player = next(player_choice)
                print(f"Current Player: {current_player}")
                played = False

                while not played:
                #int input for the entries by the players
                        column_choice = int(input("What column do you want to play? (0, 1, 2): " ))
                        row_choice = int(input("What row do you want to play? (0, 1, 2): " ))
                        
                        game, played = game_board(game, current_player, row_choice, column_choice)
                
                if win(game):
                        game_won = True
                        again = input("The game is over, would you like to play again> (y/n) ")
                        if again.lower() == "y":
                                print("restarting")
                        elif again.lower() == "n":
                                print("Byeeeeeeee")
                                play = False
                        else:
                                print("Not a valid answer, so... byyyeeeee")
                                play = False