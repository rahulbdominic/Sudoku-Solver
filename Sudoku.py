'''grid = [[1, 0, 3, 4, 0, 0, 7, 0, 9],
[0, 5, 6, 0, 8, 9, 0, 2, 3],
[0, 8, 9, 1, 0, 3, 4, 0, 6],
[2, 1, 4, 0, 6, 5, 0, 9, 7],
[3, 0, 0, 8, 0, 7, 0, 1, 4],
[8, 0, 7, 0, 1, 4, 0, 6, 5],
[0, 3, 1, 0, 4, 0, 9, 7, 8],
[6, 4, 0, 9, 7, 0, 5, 3, 1],
[0, 7, 8, 0, 0, 1, 0, 4, 2]]'''

grid=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
                      [5, 2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 8, 7, 0, 0, 0, 0, 3, 1],
                      [0, 0, 3, 0, 1, 0, 0, 8, 0],
                      [9, 0, 0, 8, 6, 3, 0, 0, 5],
                      [0, 5, 0, 0, 9, 0, 6, 0, 0],
                      [1, 3, 0, 0, 0, 0, 2, 5, 0],
                      [0, 0, 0, 0, 0, 0, 0, 7, 4],
                      [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def moveNext(x, y):
    if(x < 8):
        solve(x + 1, y)
    else:
        solve(0, y + 1)


def checkRow(x, val):
    
    for i in range(0, 9):
        if(grid[i][x] == val):
            return False
    return True

def checkColumn(y, val):

    for i in range(0, 9):
        if(grid[y][i] == val):
            return False
    return True

def checkSquare(x, y, val):

    keyX = (x + 1) % 3
    keyY = (y + 1) % 3
    if(keyX != None):
        if(keyX == 2):
            if(keyY == 2):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r - 1][y + c - 1] == val):
                            return False
                    
            if(keyY == 0):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r - 1][y + c - 2] == val):
                            return False
                    break
            if(keyY == 1):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r - 1][y + c] == val):
                            return False
                    
        if(keyX == 0):
            if(keyY == 2):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r - 2][y + c - 1] == val):
                            return False
                    
            if(keyY == 0):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r - 2][y + c - 2] == val):
                            return False
            if(keyY == 1):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r - 2][y + c] == val):
                            return False
            
        if(keyX == 1):
            if(keyY == 2):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r][y + c - 1] == val):
                            return False
                    
            if(keyY == 0):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r][y + c - 2] == val):
                            return False
                    
            if(keyY == 1):
                for r in range(3):
                    for c in range(3):
                        if(grid[x + r][y + c] == val):
                            return False

    return True

def check(x, y, val):
    #print(str(x) + "    " + str(y) + "  Val: " + str(val))
    #print(grid)
    if (checkRow(y, val) == True and checkColumn(x, val) == True and checkSquare(x, y, val) == True):
        return True

def solve(x, y): 
    
    if(y > 8):
        print (grid)
        return True
    
    if(grid[x][y] == 0):
        val = 0
        
        for val in range(1, 10):
            #print(str(x) + "    " + str(y) + "  Val: " + str(val))
            if (check(x, y, val) == True):
                grid[x][y] = val
                if(x < 8):
                    solve(x + 1, y)
                else:
                    solve(0, y + 1)
        grid[x][y] = 0
    else:
        if(x < 8):
            solve(x + 1, y)
        else:
            solve(0, y + 1)
        
    

solve(0,0)
