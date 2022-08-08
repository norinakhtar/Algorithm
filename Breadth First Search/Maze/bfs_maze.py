from collections import deque
from typing import List

class Solution:
  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    m = len(maze)
    n = len(maze[0])
    dirs = [0, 1, 0, -1, 0]
    q = deque([(start[0], start[1])])
    seen = {(start[0], start[1])}

    def isValid(x: int, y: int) -> bool:
      return 0 <= x < m and 0 <= y < n and maze[x][y] == 0

    while q:
      i, j = q.popleft()
      for k in range(4):
        x = i
        y = j
        while isValid(x + dirs[k], y + dirs[k + 1]):
          x += dirs[k]
          y += dirs[k + 1]
        if [x, y] == destination:
          return True
        if (x, y) in seen:
          continue
        q.append((x, y))
        seen.add((x, y))

    return False




if __name__ =="__main__":
    s = Solution()
    #example1
    maze1 =[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start1= [0,4]
    des1 =[4,4]
    print(s.hasPath(maze1,start1,des1))


   #example2
    maze2 =[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start2= [0,4]
    des2 =[3,2]
    print(s.hasPath(maze2,start2,des2))
    

    #example3
    maze3 =[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
    start3= [4,3]
    des3 =[0,1]
    print(s.hasPath(maze3,start3,des3))
