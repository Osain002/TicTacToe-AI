import numpy as np
from game import TicTacToe




game = TicTacToe()



class player:
        def __init__(self):

                self.Q_table = [
                        {
                                "id": 0,
                                "state": (0,0,0,0,0,0,0,0,0),
                                "q_vals": [0,0,0,0,0,0,0,0,0],
                        }
                ]
                self.actions = [0,1,2,3,4,5,6,7,8]
                self.gamma = 0.99
                self.alpha = 0.5
                self.epsilon = 0.1
        
        def choose_position(self, state):
                p = np.random.uniform(0,1)
                pos = None
                q_results = [x for x in self.Q_table if x["state"] == tuple(state)]
                if q_results == []:
                        q_results = {
                                "id": len(self.Q_table),
                                "state": tuple(state),
                                "q_vals": np.zeros(len(self.actions)),
                        }
                        self.Q_table.append(q_results)
                else:
                        q_results = q_results[0]

                if p < self.epsilon:
                        pos = np.random.choice(self.actions)
                else:
                        q = np.argmax(q_results["q_vals"])
                        pos = self.actions[q]
                return pos


        def get_max_q(self, state, actions):
                max_q = 0
                for pos in actions:
                        board = state.copy()
                        board[pos] = 1
                        Q_board = [x for x in self.Q_table if x["state"] == tuple(board)]
                        

                        if Q_board == []:
                                q_res = {
                                                "id": len(self.Q_table),
                                                "state": tuple(board),
                                                "q_vals": np.zeros(len(actions) - 1)
                                        }
                                self.Q_table.append(q_res)
                        else:
                                q_res = Q_board[0]
                        
                        q_vals = q_res["q_vals"]
                        mv = 0

                        if len(q_vals) > 0:
                                mv = max(q_vals)

                        if mv > max_q:
                                max_q = mv
                return max_q
                        


        
        def update_Q(self, pos, state, reward, actions):
                curr_state = state
                ind = actions.index(pos)
                curr_Q = [x for x in self.Q_table if x["state"] == tuple(state)][0]
                
                q_val = curr_Q["q_vals"][ind]
                max_q = self.get_max_q(curr_state, actions)
                new_q = q_val + self.alpha*(reward + self.gamma*max_q - q_val)
                
                
                self.Q_table[curr_Q["id"]]["q_vals"][ind] = new_q
                
                
        

        def train(self):
                iter = 0
                wins = 0
                loss = 0
                draws = 0
                max_iter = 10000
                while iter < max_iter:
                        state = game.reset_game()
                        self.actions = [0,1,2,3,4,5,6,7,8]
                        episode_reward = 0

                        for i in range(10):
                                pos = self.choose_position(state)
                                state_0 = state.copy()
                                actions_0 = self.actions.copy()
                                
                                
                                state, reward, done, remaining_moves = game.play_step(pos)
                                self.actions = remaining_moves
                                episode_reward += reward
                                self.update_Q(pos, state_0, reward, actions_0)
                                
                                if done:
                                        break
                        iter += 1
                        
                        if episode_reward > 99:
                                wins += 1
                        loss += game.loss
                        draws += game.draws
                        if iter%100 == 0:
                                print("won ", wins, ",draws:", draws, ",loss:", loss, ",out of", iter, "games")
                print("")
                print("==========================================")
                print("Training complete.", "Success rate:", np.floor(100*(wins/max_iter)), "%", "from", max_iter, "games")
                print("==========================================")
                print("")
                print("")
                

        def play(self):

                while True:
                        state = game.reset_game()
                        self.actions = [0,1,2,3,4,5,6,7,8]
                        episode_reward = 0
                        
                        for i in range(10):
                                pos = self.choose_position(state)
                                state_0 = state.copy()
                                actions_0 = self.actions.copy()
                                
                                
                                state, reward, done, remaining_moves = game.play_step_pl(pos)
                                self.actions = remaining_moves
                                episode_reward += reward
                                self.update_Q(pos, state_0, reward, actions_0)
                                
                                if done:
                                        break

                                
                        

                        
                                




        



player = player()

player.train()
player.play()