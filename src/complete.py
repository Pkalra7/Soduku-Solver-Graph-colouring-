import constructGraph
import cProfile
import re
import math
from constructGraph import labeledNodes
from easyThree import sudokuInstance

#this prints out the sudoku puzzle to console
def print_puzzle(sudokuInstance):
        
        for i in range(1,10):
                if (i-1)%3==0:
                        for j in range(1, 13):
                                print("_", end="")
                        print("\n")
                for k in range (1, 10):
                        if (k-1)%3==0:
                                print("|",end="")
                        print(sudokuInstance[i][k], end="")
                print("|")
                print("\n")
        for l in range(1, 13):
                print("_", end="")
        print("\n")

#picks the colour of a node permanently
def pickColour(graph,chosenV,coloured):

        #numbers represent colours
        chooseFrom=[1,2,3,4,5,6,7,8,9]
        
        for vertex in graph[chosenV]:
                if vertex in coloured:
                        if coloured[vertex] in chooseFrom:
                                chooseFrom.remove(coloured[vertex])

        assigned=False
        if len(chooseFrom)==0:
                print("out of colours to choose from")

        else:
                coloured[chosenV]=chooseFrom[0]
                assigned=True
        
        return assigned

#solves the puzzle
def completePuzzle():
        original=sudokuInstance
        print("This is your original partially filled sudoku puzzle")
        
        print_puzzle(original)
        graph=constructGraph.buildgraph(sudokuInstance)
 
        #print graph[1]
        
        #print constructGraph.colored_vertices
        
        
        coloured=labeledNodes
        
        numberOfColoured=len(labeledNodes)

        #untill all nodes are coloured
        allColoured=False
        
        while allColoured!=True:
                leader=-1
                maxSaturation=-1
                
                for i in range(1,82):
                        cNeighbours=[]
                        if i not in coloured:
                                for v in graph[i]:
                                        if v in coloured:
                                                cNeighbours.append(coloured[v])
                                cNeighbours=list(set(cNeighbours))
                                #using SDO find vertex with largest saturation degree
                                if len(cNeighbours)>maxSaturation:
                                        maxSaturation=len(cNeighbours)
                                        top=i
                                #Tie has occurred
                                elif len(cNeighbours)==maxSaturation:
                                        if len(graph[i])>len(graph[top]):
                                                top=i
                
        
                if pickColour(graph,top,coloured)==True:
                        numberOfColoured+=1
                        if numberOfColoured==81:
                                allColoured=True
                
                else:
                        print ('no Solution, Sorry')
                        return False
        
        print ('Solution exists')
        #now that we have a succesful 9 - colouring assign values to the cells of the originial sudoku grid
        for key in coloured:
                i=math.ceil(key/9)
                j=math.ceil(key%9)
                sudokuInstance[i][j]=coloured[key]
                sudokuInstance[i][9]=sudokuInstance[i][0]
        print("And This is your solution for the puzzle")
        print_puzzle(sudokuInstance)
        
        return True


        


        
