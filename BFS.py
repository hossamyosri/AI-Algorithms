from pyamaze import maze,agent,textLabel,COLOR
from collections import deque

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch= [ ]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW': #directio
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell #way to goal
                bSearch.append(childCell)
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell #place i go on  ,,path from start to goal 
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath

if __name__=='__main__':

    m=maze(5,5) #maze size
    m.CreateMaze() #to make a maze
    bSearch,bfsPath,fwdPath=BFS(m)
    a=agent(m,footprints=True,color=COLOR.yellow,filled=False,goal='c') #agent move towards the goal 
    b=agent(m,footprints=True,color=COLOR.red,filled=True) #start
    c=agent(m,1,1,footprints=True,color=COLOR.blue,filled=True,goal=(m.rows,m.cols)) #the goal
    m.tracePath({a:bSearch},delay=300,showMarked=True) #kay=agent(a) ,, value=path
    m.tracePath({c:bfsPath},delay=300 ,showMarked=True)
    m.tracePath({b:fwdPath},delay=100,showMarked=False)
    ll=textLabel(m,'A BFS Search ', len(fwdPath)+1) #numbers of steps from start to the goal
    
    m.run() 
    
print("BFS Search")
print('Done')
print("###"*70)
print("BFS Path is : ") 
print(bfsPath) #all possible point to move to
print("###"*70)
print( "FWD Path is : " ) 
print (fwdPath) #the point i cross to get the goal


