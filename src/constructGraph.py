from easyFour import sudokuInstance

labeledNodes={}

def buildgraph(sudokuInstance):

        rowVert=[]
        columnVert=[]
        subgridVert=[]
        
        rowVert=[i for i in range (1,10)]

        columnVert=[(9*i + 1) for i in range(0,9)]

        subgridVert=[1,2,3,10,11,12,19,20,21]
        
        bigGrid=[]
        
        bigGrid.append(subgridVert)
        
        firstCell=[4,7,28,31,34,55,58,61]
        
        for cell in firstCell:
                incrementBlock=cell-1
                eachSubGrid=[x+incrementBlock for x in subgridVert]
                bigGrid.append(eachSubGrid)
        

        sudokuGraph={}

         
        for vertex in range(1,82):
                sudokuGraph[vertex]=[]

        sudokuGraph=addRowEdges(sudokuGraph,rowVert)
        sudokuGraph=addColumnEdges(sudokuGraph,columnVert)
        sudokuGraph=addGridEdges(sudokuGraph,bigGrid)
        
       

                
        
        sudokuGraph=initialColouring(sudokuInstance,sudokuGraph)

        
        return sudokuGraph
        
def addRowEdges(graph,rowVert):

        r=0
        for cell in range(1,82):
                rEdges=[]
                rEdges=[9*r+x for x in rowVert]
                if cell in rEdges:
                        for num in rEdges:
                                if num!=cell:
                                        if num not in graph[cell]:
                                                graph[cell].append(num)
                                                if cell not in graph[num]:
                                                        graph[num].append(cell)
                if cell%9==0:
                        r+=1

        return graph

def addColumnEdges(graph,column):
        for cell in range(1,82):
                rEdges=column[:]
                if cell in rEdges:
                        for num in rEdges:
                                if num!=cell:
                                        if num not in graph[cell]:
                                                graph[cell].append(num)
                                                if cell not in graph[num]:
                                                        graph[num].append(cell)

                else:
                        
                        diff=cell-1
                        
                        index=0
                        
                        for j in range(0,len(rEdges)):
                                if rEdges[j]+diff<=81:
                                        rEdges[j]=rEdges[j]+diff
                                else:
                                        break
                                index=index+1
                
                        li=rEdges[:index]

                        if cell in li:
                                for num in li:
                                        if num!=cell:
                                                if num not in graph[cell]:
                                                        graph[cell].append(num)
                                                        if cell not in graph[num]:
                                                                graph[num].append(cell)
        
        
        return graph


def addGridEdges(graph,bGrid):
        for cell in range(1,82):
                for grid in bGrid:
                        if cell in grid:
                                rEdges=grid
                                for num in rEdges:
                                        if num!=cell:
                                                if num not in graph[cell]:
                                                        graph[cell].append(num)
                                                        if cell not in graph[num]:
                                                                graph[num].append(cell)
        return graph




def initialColouring(sudokuInstance,graph):
        #use global variable to use in other files
        global labeledNodes
        
        for i in range(1,10):
                for j in range(1,10):
                        if sudokuInstance[i][j]!=0:
                                labeledNodes[9*(i-1)+j]=sudokuInstance[i][j]
                               
        return graph
        

