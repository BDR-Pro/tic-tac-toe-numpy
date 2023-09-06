import numpy as np 
tie_count = 0
grid = [["Y" for i in range(3)] for j in range(3)]
row0 = grid[0]
row1 = grid[1]
row2 = grid[2]

print("Welcome to Tic Tac Toe!")
print("Player 1 is X and Player 2 is O")

def print_grid():
    print(row0)
    print(row1)
    print(row2)
    print("\n")


def finshed():
    if (row0[0] == row0[1] == row0[2] != "Y") or (row1[0] == row1[1] == row1[2] != "Y") or (row2[0] == row2[1] == row2[2] != "Y"):
        return True
    elif (row0[0] == row1[0] == row2[0] != "Y") or (row0[1] == row1[1] == row2[1] != "Y") or (row0[2] == row1[2] == row2[2] != "Y"):
        return True
    elif (row0[0] == row1[1] == row2[2] != "Y") or (row0[2] == row1[1] == row2[0] != "Y"):
        return True
    else:
        return False


def tie():
    global tie_count
    tie_count += 1
    if tie_count == 9:
        print("It's a tie!")
        return True
    
def player1():  
    while True:
        print("Player 1, enter a row and column")
        row = int(input("Row: "))
        col = int(input("Column: "))
        try:
            if grid[row][col] != "Y":
                print("That spot is already taken!")    
            else:
                grid[row][col] = "X"
                break
        except IndexError:
            print("Please enter a valid input")

def ai():
    while True:
        row = np.random.randint(3)
        col = np.random.randint(3)
        if grid[row][col] != "Y":
            print("That spot is already taken!")    
        else:
            grid[row][col] = "O"
            break


def player2():  
    while True:
        try:
            print("Player 2, enter a row and column")
            row = int(input("Row: "))
            col = int(input("Column: "))
            if grid[row][col] != "Y":
                print("That spot is already taken!")    
            else:
                grid[row][col] = "O"
                break
        except IndexError:
            print("Please enter a valid input")


def playerorai():
    while True:
        player = input("Would you like to play against a player or an AI? (p/a)")
        if player == "p":
            return  True
        elif player == "a":
            ai()
            return False
        else:
            print("Please enter a valid input")

def whotoplay(ans):
    if ans:
        player2()
    else:
        ai()


ans=playerorai()
while(finshed() is False):
    print_grid()
    player1()
    if(finshed()):break
    if(tie()):break
    print_grid()
    whotoplay(ans)
    if(tie()):break
    print_grid()


print("Game over!")
