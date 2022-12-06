import numpy as np

class TicTacToe:
        def __init__(self):
                self.board = [0,0,0,0,0,0,0,0,0]
                self.moves_left = [0,1,2,3,4,5,6,7,8]
                self.player = 1
                self.reward = 0
                self.done = False
                self.draws = 0
                self.loss = 0

                self.cells = {
                                1:[],
                                2:[]
                        }
                self.wins = [[0,1,2],[3,4,5],[6,7,8],
                        [0,3,6],[1,4,7],[2,5,8],
                        [0,4,8],[2,4,6]]
        
        def reset_game(self):
                self.__init__()
                return self.board
        
        def get_state(self):
                return self.board

        def detect_win(self, cells):
                w = False
                for win in self.wins:
                        if set(win).issubset(cells):
                                w = True
                if w and self.player == 1:
                       
                        self.reward += 100
                        self.done = True
                        
                elif w and self.player ==2:
                        self.loss += 1
                        self.reward -= 100
                        self.done = True
                
                if all(x != 0 for x in self.board) and not self.done:
                      
                        self.reward += 5
                        self.draws += 1
                        self.done = True
        

        def place_token(self, pos):
                

                self.cells[self.player].append(pos)
                self.board[pos] = self.player
                self.moves_left.remove(pos)
                player_cells = self.cells[self.player]
                
                self.detect_win(player_cells)

                if self.player == 1:
                        self.player = 2
                else:
                        self.player = 1
                
        
        def randy(self):
                pos = None
                if self.moves_left != []:
                        pos = np.random.choice(self.moves_left)
                return pos
        
        def play_step(self, pos):               
                self.place_token(pos)
                if not self.done:
                        p2_pos = self.randy()
                        if p2_pos != None:
                                self.place_token(p2_pos)
                        else:
                                self.done = True
                state = self.get_state()
                return state, self.reward, self.done, self.moves_left
        
        def print_board(self):
                board = np.reshape(self.board, (3,3))
                print(board)
        
        def play_step_pl(self, pos):               
                self.place_token(pos)
                self.print_board()

                if not self.done:
                        

                        p2_pos = int(input("Player 2: "))
                        self.place_token(p2_pos)

                state = self.get_state()
                return state, self.reward, self.done, self.moves_left
        


# game = TicTacToe()

# while True:
#         pos = int(input("S:"))
#         state, reward, done, moves = game.play_step(pos)
#         print(state, reward, done, moves)
#         if done:
#                 break
        

        
                
        
        


