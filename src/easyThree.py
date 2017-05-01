
"Particular Sudoku Instance"
"Easy Level!"
"Easy testcase #1"


def print_puzzle(sudokuInstance):
        
        for i in range(1,rows+1):
                if (i-1)%3==0:
                        for j in range(1, 13):
                                print("_", end="")
                        print("\n")
                for k in range (1, rows+1):
                        if (k-1)%3==0:
                                print("|",end="")
                        print(sudokuInstance[i][k], end="")
                print("|")
                print("\n")
        for l in range(1, 13):
                print("_", end="")
        print("\n")

#initialize Sudoku array of rows
sudokuInstance=[]

rows=9

#Transform array into 2D array/grid and initialze all cell values to 0
#We're using 10 rows and columns to be able to use index 9 for simplicity purposes
for row in range(0,rows+1):
	cellVal=[0 for col in range(0,rows+1)]
	sudokuInstance.append(cellVal)

sudokuInstance[1][1]=5
sudokuInstance[1][3]=8
sudokuInstance[1][8]=6

sudokuInstance[2][2] = 4
sudokuInstance[2][3] = 2
sudokuInstance[2][6] = 8
sudokuInstance[2][9] = 3

sudokuInstance[3][1] = 6
sudokuInstance[3][3] = 3
sudokuInstance[3][5] = 4
sudokuInstance[3][6] = 9
sudokuInstance[3][9] = 7

sudokuInstance[4][1] = 8
sudokuInstance[4][3] = 9
sudokuInstance[4][5] = 3

sudokuInstance[5][1] = 3
sudokuInstance[5][2] = 7
sudokuInstance[5][4] = 2
sudokuInstance[5][6] = 1
sudokuInstance[5][8] = 4
sudokuInstance[5][9] = 8

sudokuInstance[6][5] = 8
sudokuInstance[6][7] = 3
sudokuInstance[6][9] = 2

sudokuInstance[7][1] = 2
sudokuInstance[7][4] = 1
sudokuInstance[7][5] = 5
sudokuInstance[7][7] = 4
sudokuInstance[7][9] = 9

sudokuInstance[8][1] = 1
sudokuInstance[8][4] = 4
sudokuInstance[8][7] = 2
sudokuInstance[8][8] = 5

sudokuInstance[9][2] = 5
sudokuInstance[9][7] = 7
sudokuInstance[9][9] = 1





        
#print_puzzle(sudokuInstance)
