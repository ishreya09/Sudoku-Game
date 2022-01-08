import random
from tabulate import tabulate

grid=[]
for i in range(9):
    grid.append([0,0,0,0,0,0,0,0,0])

#print (grid)

def inrow(testval,row,col):
    if testval in grid[row]:
        #print(testval,"in row")
        return True
    else:
        #print(testval,"not in row")
        return False


def incolumn(testval,row,col):
    colList=[]
    for i in range(9):
        colList.append(grid[i][col])
    #print("col",colList)
    if testval in colList:
        return True
    else:
        return False

def square(testval,row,col):
    square=[]

    if row < 3:
        if col < 3:
            square = [grid[i][0:3] for i in range(0, 3)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(0, 3)]
        else:
            square = [grid[i][6:9] for i in range(0, 3)]
    elif row < 6:
        if col < 3:
            square = [grid[i][0:3] for i in range(3, 6)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(3, 6)]
        else:
            square = [grid[i][6:9] for i in range(3, 6)]
    else:
        if col < 3:
            square = [grid[i][0:3] for i in range(6, 9)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(6, 9)]
        else:
            square = [grid[i][6:9] for i in range(6, 9)]

    #print ("square",square)

    return bool(testval in square[0]+square[1]+square[2])

def isGridFilled(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                return False
    else:
        return True

def generate(grid,tracker):
    value=[1,2,3,4,5,6,7,8,9]
    for cell in range(81):
        a=random.shuffle(value)
        #print ("a",value)
        row=cell//9
        col=cell%9
        if grid[row][col] == 0:

            for testval in value:
                a=inrow(testval,row,col)
                b=incolumn(testval,row,col)
                c=square(testval,row,col)

                if a==False and b==False and c==False:
                    #print("assigning")
                    grid[row][col]=testval
                    #print(tabulate(grid,tablefmt="fancy_grid"))
                    if isGridFilled(grid):
                        return True
                    else:
                        if generate(grid, cell):
                            return True

            break 
    grid[row][col] = 0

    

def Printgrid(Grid):
    print(tabulate(grid,tablefmt="fancy_grid"))


def main():
    global grid
    generate(grid,1)
    Printgrid(grid)
    return grid


if __name__=="__main__":
    main()

