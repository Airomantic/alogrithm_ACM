

class Solution:
    # def __init__(self):
    #     self.flag=[[0]*col]*row
    #     self.path=[[1]*col]*row

    def dfs(self,cur_i, cur_j,dem):
        _dir_ = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if path[cur_i][cur_j]>1:
            return path[cur_i][cur_j]
        bf=path[cur_i][cur_j] #构成接力
        for di,dj in _dir_:
            next_i,next_j=cur_i+di,cur_j+dj
            if 0 <= next_i < row and 0 <= next_j < col and flag[next_i][next_j]==0 and dem[next_i][next_j] < dem[cur_i][cur_j] :

                flag[next_i][next_j]=1
                path[cur_i][cur_j]=max(path[cur_i][cur_j],bf+self.dfs(next_i,next_j,dem))
                print(dem[next_i][next_j])
                flag[next_i][next_j]=0 #恢复

        return path[cur_i][cur_j]

    def HuaXue(self,dem):
        ans=1
        for i in range(row):
            for j in range(col):
                flag[i][j]=1
                ans = max(self.dfs(i, j,dem), ans)
                flag[i][j]=0 #恢复
        return ans

while True:
    n=list(map(int,input().strip().split(" ")))
    row,col=n[0],n[1]

    dem=[[]*col]*row
    flag=[[0]*col]*row
    path=[[1]*col]*row

    for i_row in range(row):
        dem[i_row]=list(map(int,input().strip().split(" ")))
    res=Solution().HuaXue(dem)
    print(res)