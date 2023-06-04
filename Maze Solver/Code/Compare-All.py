from BFS import *
from DFS import *
from aStar import *
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

m=maze(20,30)
m.CreateMaze(loopPercent=100)
searchPath,dfsPath,fwdDFSPath=DFS(m)
bSearch,bfsPath,fwdBFSPath=BFS(m)
ASearch,Apath,fwdAPath=aStar(m)

l=textLabel(m,'DFS Path Length',len(fwdDFSPath)+1)
l=textLabel(m,'BFS Path Length',len(fwdBFSPath)+1)
l=textLabel(m,'A-Star Path Length',len(fwdAPath)+1)
l=textLabel(m,'DFS Search Length',len(searchPath)+1)
l=textLabel(m,'BFS Search Length',len(bSearch)+1)
l=textLabel(m,'A-Star Search Length',len(searchPath)+1)

a=agent(m,footprints=True,color=COLOR.cyan,filled=True)
b=agent(m,footprints=True,color=COLOR.yellow,filled=True)
c=agent(m,footprints=True,color=COLOR.blue,shape='arrow')

m.tracePath({a:fwdDFSPath},delay=100)
m.tracePath({b:fwdBFSPath},delay=100)
m.tracePath({c:fwdAPath},delay=100)


t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
t2=timeit(stmt='BFS(m)',number=1000,globals=globals())
t3=timeit(stmt='aStar(m)',number=1000,globals=globals())

textLabel(m,'DFS Time',t1)
textLabel(m,'BFS Time',t2)
textLabel(m,'A-Star Time',t3)

m.run()