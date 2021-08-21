m = int(input())
grid = [[] for i in range(m)]
for i in range(m):
    line = input().split(' ')
    for j in range(len(line)):
        grid[i].append(int(line[j]))
print(grid)