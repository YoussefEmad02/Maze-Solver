from pyamaze import maze,agent,COLOR
def DFS(m,start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==(1,1):
            break
        poss = 0
        for d in 'ESNW':
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
                poss += 1
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath


if __name__=='__main__':
    m=maze()
    m.CreateMaze()
    dSeacrh,dfsPath,fwdPath=DFS(m)
    a=agent(m,footprints=True)
    m.tracePath({a:fwdPath})
    m.run()

