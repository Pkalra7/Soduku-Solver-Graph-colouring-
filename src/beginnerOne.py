
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

sudokuInstance[1][3]=6
sudokuInstance[1][7]=5
sudokuInstance[1][9]=8

sudokuInstance[2][1] = 1
sudokuInstance[2][3] = 2
sudokuInstance[2][4] = 3
sudokuInstance[2][5] = 8
sudokuInstance[2][9] = 4

sudokuInstance[3][4] = 2
sudokuInstance[3][7] = 1
sudokuInstance[3][8] = 9

sudokuInstance[4][5] = 6
sudokuInstance[4][6] = 3
sudokuInstance[4][8] = 4
sudokuInstance[4][9] = 5

sudokuInstance[5][2] = 6
sudokuInstance[5][3] = 3
sudokuInstance[5][4] = 4
sudokuInstance[5][6] = 5
sudokuInstance[5][7] = 8
sudokuInstance[5][8] = 7

sudokuInstance[6][1] = 5
sudokuInstance[6][2] = 4
sudokuInstance[6][4] = 9
sudokuInstance[6][5] = 2

sudokuInstance[7][2] = 8
sudokuInstance[7][3] = 7
sudokuInstance[7][6] = 4

sudokuInstance[8][1] = 2
sudokuInstance[8][5] = 9
sudokuInstance[8][6] = 8
sudokuInstance[8][7] = 4
sudokuInstance[8][9] = 7

sudokuInstance[9][1] = 4
sudokuInstance[9][3] = 9
sudokuInstance[9][7] = 3





        
#print_puzzle(sudokuInstance)
