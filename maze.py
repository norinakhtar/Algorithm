from typing import List
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
       directions= [(1,0),(-1,0),(0,-1),(0,1)]
       m = len(maze)
       n = len(maze[0])

       stack =[]
       seen = set()
       stack.append((start[0],start[1]))
       seen.add((start[0],start[1]))
       while stack:
           cur_i,cur_j =stack.pop()
           for d in directions:
               ni = cur_i
               nj = cur_j
               while 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == 0:
                   ni += d[0]
                   nj += d[1]

               ni -= d[0]
               nj -= d[1]

               if ni == destination[0] and nj == destination[1]:
                   return True

               if(ni,nj) not in seen:
                    stack.append((ni,nj))
                    seen.add((ni,nj))
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

            

       