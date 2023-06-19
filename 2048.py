import random
def init2048 ():
    grid = []
    for row in range (4):
        newRow = []
        for value in range (4):
            newRow.append(" ")
        grid.append(newRow)
    return grid

def newNum(grid):
    randomRow = random.randint(0,3)
    randomCol = random.randint(0,3)
    randomValue = random.randint(1,2)
    while grid[randomRow][randomCol] != " ":
        randomRow = random.randint(0,3)
        randomCol = random.randint(0,3)
    if randomValue == 1:
        grid[randomRow][randomCol] = 2
    else:
        grid[randomRow][randomCol] = 4
    return grid

def shiftLeft (grid):
    for row in grid:
        
        for num in range (4):
            if row[num] != " ":
              
               #add numbers together
                if num + 1 <= 3 :
                    if row[num+1] == row[num]:
                        row[num] = 2 * row[num]
                        row[num+1] = ' '
                #shift numbers to the left
                i = num
                while i >= 1 and row[i-1]== ' ':
                    row[i-1] = row[i]
                    row[i] = " "
                    i = i-1 
                    
    return grid

def shiftRight(grid):
    for row in grid:
        a = 3
        while a >= 0:
            if row[a] != " ":
                if row[a-1] == row [a]:
                    row[a] = 2 * row[a]
                    row[a-1] = ' '
                
                i = a
                while i <= 2 and row[i+1]== ' ':
                    row[i+1] = row[i]
                    row[i] = " "
                    i = i+1 
            a = a-1

    return grid

def shiftUp(grid):
    for col in range(4):
        for row in range (4):
            if grid[row][col] != " ":
                #add numbers
                if row + 1 <= 3 or row + 2 <= 3:
                    if grid[row+1][col] == grid[row][col]:
                        grid[row][col] = 2 * grid[row][col]
                        grid[row+1][col] = ' '
                    
                #shift up
                i = row
                while i >= 1 and grid[i-1][col] == " ":
                    grid[i-1][col] = grid[i][col]
                    grid[i][col] = ' '
                    i = i-1
    return grid

def shiftDown(grid):
    for col in range (4):
        a = 3
        while a >= 0:
            if grid[a][col] != " ":
                if grid[a-1][col] == grid[a][col]:
                    grid[a][col] = 2 * grid[a][col]
                    grid[a-1][col] = ' '
                i = a
                while i <= 2 and grid[i+1][col] == " ":
                    grid[i+1][col] = grid[i][col]
                    grid[i][col] = ' '
                    i = i + 1
            a = a - 1
    return grid

def displayBoard(grid):
     for row in grid :
        # Build up the string for the row
        rowString = ""
        # Loop through the values in the row
        for value in row :
            # Add one value to the string
            rowString = rowString + str(value) + " | "
        # Print out the entire row
        print (rowString)
        print ("--------------")


#grid1 = [[' ', ' ', ' ', ' '], [' ', ' ', 2, ' '], [' ', ' ',' 3', ' '], [' ', ' ',' ', 4]]
#print(shiftLeft(grid1))
#print(shiftRight(grid1))
#print(shiftUp(grid1))
#print(shiftDown(grid1))

def main():
    board2048 = init2048()
    board2048 = newNum(board2048)
    board2048 = newNum(board2048)
    displayBoard(board2048)
    user_input = input('Enter "a" to shift left, "d" to shift right, "w" to shift up, "s" to shift down, or "quit" to end the game')
    while user_input != 'quit':
        if user_input == 'a':
            board2048 = shiftLeft(board2048)
            board2048 = newNum(board2048)
            displayBoard(board2048)
        elif user_input == 'd':
            board2048 = shiftRight(board2048)
            board2048 = newNum(board2048)
            displayBoard(board2048)
        elif user_input == 'w':
            board2048 = shiftUp(board2048)
            board2048 = newNum(board2048)
            displayBoard(board2048)
        elif user_input == 's':
            board2048 = shiftDown(board2048)
            board2048 = newNum(board2048)
            displayBoard(board2048)
        else:
            print('Try again')
        user_input = input('Enter "a" to shift left, "d" to shift right, "w" to shift up, "s" to shift down, or "quit" to end the game')
    if user_input == 'quit':
        print("You lost")
    


main()
    