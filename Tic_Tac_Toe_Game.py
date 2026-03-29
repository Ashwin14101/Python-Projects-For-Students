import tkinter as tk # we are referring tkinter as tk.
from tkinter import messagebox

class TicTacToe: # We are creating a class for our complete game. In our class, we sort class data as our important data.
    def __init__(self): # For Initialize kosam init fucntion or method is define
        self.current_player = "X" # we create data items/elements and intialize them.
        self.board = [["","",""],["","",""],["","",""]] # we create a grid in tkinter library window, that grid is created by board. (board==grid )
        self.window = tk.Tk() # We also create a window, We Initialized the Window using tkinter.
        self.window.title("Tic Tac Toe") # We give window name

        self.buttonGrid = []
        for i in range(3): # motham 3 rows ni create chestadi. aa 3 rows kalipethe grid avvutadhi.
            row = [] # prathi i ki gannu oka row ni create chedammu.
            for j in range(3): # prathi row lo nu manaku 3 individual button kavali.
                button = tk.Button(self.window,text="",width=5,height=5,command= lambda i=i,j=j: self.make_move(i,j)) # anni add chedammu, tk button dintilo manam ee window lo attach cheyali.
                button.grid(row=i,column=j) # tk button has property is grid, tells what is the position of the button.
                row.append(button)
            self.buttonGrid.append(row) # row ni append chestammu.

    def make_move(self,row,col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttonGrid[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo(
                    "Game Over", 
                    f"the Winner is {self.current_player}"
                )
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo(
                "Game Over",
                "Its a Draw"
                )
                self.window.quit()
                
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self,player):
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if player == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        
        return False
    
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    # Intialization of the complete game is succesfully created.

    def run(self): # We define run to run the application.
        self.window.mainloop()

game = TicTacToe()
game.run()