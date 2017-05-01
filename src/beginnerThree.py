
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

sudokuInstance[1][3]=3
sudokuInstance[1][4]=1
sudokuInstance[1][6]=5
sudokuInstance[1][8]=7

sudokuInstance[2][3] = 2
sudokuInstance[2][5] = 9
sudokuInstance[2][6] = 7
sudokuInstance[2][7] = 8

sudokuInstance[3][2] = 5
sudokuInstance[3][5] = 8
sudokuInstance[3][6] = 4
sudokuInstance[3][7] = 9
sudokuInstance[3][9] = 2

sudokuInstance[4][2] = 4
sudokuInstance[4][4] = 2
sudokuInstance[4][7] = 3

sudokuInstance[5][2] = 2
sudokuInstance[5][4] = 5
sudokuInstance[5][6] = 9
sudokuInstance[5][8] = 4

sudokuInstance[6][3] = 9
sudokuInstance[6][6] = 3
sudokuInstance[6][8] = 1

sudokuInstance[7][1] = 2
sudokuInstance[7][3] = 4
sudokuInstance[7][4] = 7
sudokuInstance[7][5] = 5
sudokuInstance[7][8] = 8

sudokuInstance[8][3] = 6
sudokuInstance[8][4] = 4
sudokuInstance[8][5] = 1
sudokuInstance[8][7] = 5

sudokuInstance[9][2] = 1
sudokuInstance[9][4] = 9
sudokuInstance[9][6] = 8
sudokuInstance[9][7] = 6





        
#print_puzzle(sudokuInstance)
