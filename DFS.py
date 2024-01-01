from Pyamaze import maze,agent,textLabel,COLOR
textLabel = "DFS Search"
def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW': #direction
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    
    m=maze (8,6) # Change to any size
    m.CreateMaze(1,4) # (2,4) is Goal Cell, Change that to any other valid cell

    dSeacrh,dfsPath,fwdPath=DFS(m,(2,1)) # (5,1) is Start Cell, Change that to any other valid cell

    a=agent(m,2,1,goal=(1,4),footprints=True,shape='square',color=COLOR.blue)
    b=agent(m,1,4,goal=(2,1),footprints=True,filled=True)
    c=agent(m,2,1,footprints=True,color=COLOR.yellow)
    m.tracePath({a:dSeacrh},showMarked=True)
    m.tracePath({b:dfsPath})
    m.tracePath({c:fwdPath})
    m.run()
    
    
    
#     function BREADTH-FIRST-SEARCH(initialState, goal'Test)
# returns SUCCESS or FAILURE :

# frontier Queue.new (initialState)
# explored = Set.new()

# while not frontier.isEmpty ():
# state = frontier.dequeue()
# explored.add(state)

# if goalTest(state):
# return SUCCESS(state)

# for neighbor in state.neighbors():
# if neighbor not in frontier U explored:
# frontier.enqueue(neighbor)

# return FAILURE
