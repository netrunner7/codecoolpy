# # tictactoe
# board = "|_|_|_|\n|_|_|_|\n|_|_|_|"

def printmove(player_move , board, char):
    index = 0
    char = char
    player_move = player_move
    if player_move == 1:
        index = 1
    if player_move == 2:
        index = 3
    if player_move == 3:
        index = 5
    if player_move == 4:
        index = 9
    if player_move == 5:
        index = 11
    if player_move == 6:
        index = 13
    if player_move == 7:
        index = 17
    if player_move == 8:
        index = 19
    if player_move == 9:
        index = 21
    board = board[0:index] + char + board[index + 1:]
    print(board)
    return board

def main():
    import time
    import os
    # Intro
    print('''
__________     ___.  ___.                  ________                 __    
\______   \__ _\_ |__\_ |__   ___________  \______ \  __ __   ____ |  | __
 |       _/  |  \ __ \| __ \_/ __ \_  __ \  |    |  \|  |  \_/ ___\|  |/ /
 |    |   \  |  / \_\ \ \_\ \  ___/|  | \/  |    `   \  |  /\  \___|    < 
 |____|_  /____/|___  /___  /\___  >__|    /_______  /____/  \___  >__|_  |
        \/          \/    \/     \/                \/            \/     \/
    ''')
    time.sleep(2)
    os.system('clear')
    print("Presents:")
    time.sleep(2)
    os.system('clear')
    print('''
__ __|_)      __ __|          __ __|          
   |   |  __|    |  _` |  __|    |  _ \   _ \ 
   |   | (       | (   | (       | (   |  __/ 
  _|  _|\___|   _|\__,_|\___|   _|\___/ \___|   
    ''')
    time.sleep(2)
    print('''
    Possible moves: 1, 2, 3, 4, 5, 6, 7, 8, 9 ; try to fill a row!
    |_|_|_|     =     1 | 2 | 3
    |_|_|_|     =     4 | 5 | 6
    |_|_|_|     =     7 | 8 | 9
    ''')
    board = "|_|_|_|\n|_|_|_|\n|_|_|_|"
    char = "X"
    playeronethinking = True
    possible_moves = [1,2,3,4,5,6,7,8,9]
    player_one_moves = []
    player_two_moves = []    

    wining_moves = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9] , [1 , 5 , 9] , [ 7, 5, 3] , [1 , 4 , 7] , [2 , 5 , 8] , [3 , 6 , 9]]
    endgame = False

    while endgame != True:
        #1 ruch gracza 1 ( X )
        while playeronethinking == True:
            badmove = False
            char = "X"
            isCorrect = False
            while isCorrect == False:
                player_move_str = input("Player One - please make your move:")
                try:
                    player_move = int(player_move_str)
                    isCorrect = True
                except ValueError:
                    print("This is not a number!")
                    
            try:
                possible_moves.index(player_move)
                possible_moves.remove(player_move)
                player_one_moves.append(player_move)
                print("\n")
                board= printmove(player_move , board , char)
                print("\n")
            except:
                print("Move not possible")
                badmove = 1
            if badmove == 1:
                continue
            playeronethinking = False
            playertwothinking = True
            for x in range(0, 8):
                if list(set(wining_moves[x]).intersection(set(player_one_moves))):
                    list_0=list(set(wining_moves[x]).intersection(set(player_one_moves)))
                    if len(list_0) == 3:
                        print("Player One Wins!")
                        endgame = True
                        
            if not possible_moves:
                print("Tie")
                endgame = True
       
        #2 ruch gracza 2 ( o )
        while playertwothinking == True:
            if endgame == True:
                break
            badmove = 0
            char = "O"
            isCorrect = False

            while isCorrect == False:
                player_move_str = input("Player Two - please make your move:")
                try:
                    player_move = int(player_move_str)
                    isCorrect = True
                except ValueError:
                    print("This is not a number!")
            try:
                possible_moves.index(player_move)
                possible_moves.remove(player_move)
                player_two_moves.append(player_move)
                print("\n")
                board= printmove(player_move , board , char)
                print("\n")
            except:
                print("Move not possible")
                badmove = 1
            if badmove == 1:
                continue
            playertwothinking = False
            playeronethinking = True

            for x in range(0, 8):
                if list(set(wining_moves[x]).intersection(set(player_two_moves))):
                    list_0=list(set(wining_moves[x]).intersection(set(player_two_moves)))
                    if len(list_0) == 3:
                        print("Player Two Wins!")
                        endgame = True

            if not possible_moves:
                print("Tie")
                endgame = True

    
main()

