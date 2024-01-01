
import curses
from curses import wrapper
from queue import LifoQueue
import time


maze = [
    ["#","#","#","#","#","#","#","#"],
    ["#","A",".",".","#",".",".","#"],
    ["#",".","#",".","#",".","#","#"],
    ["#",".",".",".",".",".",".","#"],
    ["#","#","#",".","#","#",".","#"],
    ["#",".",".",".",".",".","B","#"],
    ["#","#","#","#","#","#","#","#"],
]

def find_start(maze , start):
    for i , row in enumerate(maze):
        for j , value in enumerate(row):
         if value == start:
          return i , j
    return None     

def find_path(maze , stdscr):
    start = "A"
    end = "B"
    start_pos = find_start(maze , start)
    
    q= LifoQueue()
    q.put((start_pos , [start_pos]))

    visited = set()

    while not q.empty():
        current_pos , path = q.get()
        row , col = current_pos
        
        stdscr.clear()
        print_maze(maze ,stdscr , path)
        time.sleep(0.0)
        stdscr.refresh()
         
        if maze[row][col]== end:
         return path

        nighbors = find_nighbors(maze , row , col)
        for nighbor in nighbors:
            if nighbor in visited:
             continue

            r , c = nighbor
            if maze[r][c]=="#":
                continue

            new_path = path+[nighbor]
            q.put((nighbor , new_path))
            visited.add(nighbor)

def find_nighbors(maze , row , col):
    nighbors = []
    if row >0: #up
        nighbors.append((row-1 , col))
    if row+1 < len(maze): #down
        nighbors.append((row+1 , col))
    if col >0: #left
        nighbors.append((row , col-1))
    if col+1 < len(maze[0]): #right
        nighbors.append((row , col+1)) 
    return nighbors    

def print_maze(maze,stdscr ,path=[]):
    BLUE =curses.color_pair(1)
    RED =curses.color_pair(2)
   
    for i , row in enumerate(maze):
        for j , value in enumerate(row):
            if (i , j) in path:
             stdscr.addstr(i,j*2,"♥" , RED)    
            else:    
             stdscr.addstr(i,j*2,value , BLUE) 

def main(stdscr):
    curses.init_pair(1 , curses.COLOR_BLUE ,curses.COLOR_BLACK)
    curses.init_pair(2 , curses.COLOR_RED ,curses.COLOR_BLACK)
    color1 =curses.color_pair(1)
    color1 =curses.color_pair(2)
    find_path(maze , stdscr)
    stdscr.getch()

wrapper(main)    