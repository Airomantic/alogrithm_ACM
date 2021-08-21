

class Solution:
    def __init__(self):
        self.flag=[[0]*col]*row
        self.path=[[1]*col]*row

    def dfs(self,cur_i, cur_j, dem):
        _dir_ = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ians = 1
        count=0
        for di, dj in _dir_:
            next_i, next_j = cur_i + di, cur_j + dj
            if 0 <= next_i < row and 0 <= next_j < col:
                if dem[next_i][next_j] < dem[cur_i][cur_j]:
                    print("路线=",dem[next_i][next_j],dem[cur_i][cur_j])
                    ians += self.dfs(next_i, next_j, dem)
            break #当不满足条件时可能不会自动跳出本次某点开始的循环
                # print("dem[next_i][next_j]=", dem[next_i][next_j])
        return ians

    # ians = 1  # 重新从1开始，覆盖原来
    def HuaXue(self,dem):
        row, col = len(dem), len(dem[0])
        ans = 0

        for i in range(row):
            for j in range(col):
                ans = max(self.dfs(i, j, dem), ans)
        return ans

while True:
    n=list(map(int,input().strip().split(" ")))
    row,col=n[0],n[1]
    # ians=0
    dem=[[]*col]*row
    for i_row in range(row):
        dem[i_row]=list(map(int,input().strip().split(" ")))
    res=Solution().HuaXue(dem)
    print(res)