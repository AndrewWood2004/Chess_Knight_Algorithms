from graph import Graph, Node
from a_star import AStar
import bfs
import dfs
import numpy as np
import Dijkstra
import time

def run():
    bdSize = 8
    start = input(f"Please enter a number between 0 and {(bdSize**2)-1} to start: ")
    target = input(f"Please enter a number between 0 and {(bdSize**2)-1} to finish: ")
    # Create graph
    graph = Graph()
    visual = np.zeros((bdSize, bdSize))
    visualpath = []
    BFSPath=[]
    DFSPath=[]
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = str(posToNodeId(row, col, bdSize))
            newPositions = genLegalMoves(row, col, bdSize)
            if graph.find_node(posToNodeId) == None:
              graph.add_node(Node(nodeId, (row,col)))
            for i in newPositions:
              newX = i[0]
              newY = i[1]
              nid = str(posToNodeId(newX, newY, bdSize))
              if graph.find_node(nid) == None:
                graph.add_node(Node(nid, (newX,newY)))
              graph.add_edge(nodeId, nid)
      
    # Execute the algorithm
    #A* start
    startAStarTime=time.time()
    alg = AStar(graph, start, target)
    path, path_length = alg.search()
    for i in graph.nodes:
      if i in path:
        visualpath.append(i)
    for r in visualpath:
      visual[r.x, r.y] = 1
    exeTimeAStar=time.time()-startAStarTime
    #End A*
    
    #Setup for BFS and DFS
    endBFSY=int(path[-1])%8
    endBFSX=int((int(path[-1])-endBFSY)/8)
    
  
    knightpos=[visualpath[0].x+1,visualpath[0].y+1]
    targetpos=[endBFSX+1,endBFSY+1]
    
  
    print(" -> ".join(path))
    
    print(f"Length of the path: {int(path_length/2)}")
    print(visual)
    print("The Dijkstra algorithm takes the path: " ,end='')

    #Dijkstra Start
    startDijkstraTime=time.time()
    Dijkstra.DijkstraAlg(start,target)
    exeDijkstraTime=time.time()-startDijkstraTime
    #End Dijkastra
  
    #Breadth First Start
    startBFSTime=time.time()
    pointAtoB, fullGraph = bfs.minStepToReachTarget(knightpos, targetpos, bdSize)
    exeBFSTime=time.time()-startBFSTime
  
    for x in fullGraph[1:]:
        
        for y in x[1:]:
            if (y == None):
                print("X",end=" \u001b[37m")
            else:
                print(y,end=" \u001b[37m")
        print()
    currentCell= pointAtoB
    print()
    while currentCell!=None:
        xAndYMove=[currentCell.x,currentCell.y]
        BFSPath.insert(0,xAndYMove)
        currentCell=currentCell.prevCell
  
    print("The path taken by Breadth First was ", end="")

    for x in BFSPath:
      
        print(x, end= " ")
    print()
    print()
  	
    print("It took " + str(pointAtoB.dist) + " steps")
    #End Breadth first

    #Depth First start
    startDFSTime=time.time()
    pointAtoB, fullGraph = dfs.minStepToReachTarget(knightpos, targetpos, bdSize)
    exeDFSTime=time.time()-startDFSTime
  
    for x in fullGraph[1:]:
        
        for y in x[1:]:
            if (y == None):
                print("X",end=" \u001b[37m")
            else:
                print(y,end=" \u001b[37m")
        print()
    currentCell= pointAtoB
    print()
    while currentCell!=None:
        xAndYMove=[currentCell.x,currentCell.y]
        DFSPath.insert(0,xAndYMove)
        currentCell=currentCell.prevCell
  
    print("The path taken by Depth First was ", end="")

    for x in BFSPath:
      
        print(x, end= " ")
    print()
    print()
  	
    print("It took " + str(pointAtoB.dist) + " steps")
  
    print()
    print("A* took " +str(exeTimeAStar)+ " seconds")
    print("Dijkstra took " + str(exeDijkstraTime)+" seconds")
    print("Breadth First Search took "+ str(exeBFSTime)+" seconds")
    print("Depth FIrst took "+ str(exeDFSTime)+" seconds")
    
    

def posToNodeId(row, col, bdSize):
    return (row * bdSize) + col

def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                           (1, -2), (1, 2), (2, -1), (2, 1)]
    for item in moveOffsets:
        newX = x + item[0]
        newY = y + item[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


if __name__ == '__main__':
    run()
    

