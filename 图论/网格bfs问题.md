## 网格图bfs问题—-该章节序号

**994 1765**

🍔网格图dfs,bfs题单：

[分享丨【算法题单】网格图（DFS/BFS/综合应用） - 讨论 - 力扣（LeetCode）](https://leetcode.cn/discuss/post/3580195/fen-xiang-gun-ti-dan-wang-ge-tu-dfsbfszo-l3pa/)

## 万能模板

📋bfs问题不用单独写一个bfs函数 也不用递归，直接在while循环里写就行

很多**网格类 BFS 问题**（最短路径、扩散、岛屿、感染）都可以套这个模板：

```c++
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int bfsGrid(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    queue<pair<pair<int,int>,int>> q;
    
    // 初始化状态：入队起点
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(/* 判断起点条件 */){
                q.push({{i,j},0});
            }
        }
    }

    int result = 0;
    
    while(!q.empty()){
        auto tmp = q.front(); q.pop();
        int x = tmp.first.first;
        int y = tmp.first.second;
        int step = tmp.second;

        // 更新结果
        result = max(result, step);

        for(int k = 0; k < 4; k++){
            int nx = x + dx[k];
            int ny = y + dy[k];

            if(nx >= 0 && nx < n && ny >= 0 && ny < m && /* 可扩展条件 */){
                // 标记已访问 / 更新状态
                grid[nx][ny] = /* 新状态 */;
                q.push({{nx, ny}, step + 1});
            }
        }
    }

    // 可加后处理
    return result;
}

```

**队列元素保存状态 + 步数**

**dx/dy 遍历四个方向**

**边界检查 + 条件判断**

**入队同时更新状态，避免重复访问**

**最后判断剩余目标（如新鲜橘子、未访问点）**

## 题目



### 994. 腐烂的橘子

[994. 腐烂的橘子 - 力扣（LeetCode）](https://leetcode.cn/problems/rotting-oranges/description/?envType=study-plan-v2&envId=top-100-liked)

✅在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；
- 值 `1` 代表新鲜橘子；
- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`* 。



✒️无论是dfs还是bfs访问后都得标记啊！！！！！！！！！！！

在这个题目里，队列中的一个状态需要包括三个值，位置x位置y和腐烂的分钟，**BFS + 队列 + 坐标 + 时间记录。**

**BFS 不需要单独写一个 `bfs()` 函数**

- 直接在 while 循环里腐烂周围橘子即可

**分钟数计算**

- 每个队列元素保存腐烂时间 `t`，更新 `minutes = max(minutes, t)`

**新鲜橘子计数**

- 遍历结束后，如果 `fresh > 0`，说明有橘子永远不会腐烂 → 返回 -1

```c++
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
private:
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

public:
    int orangesRotting(vector<vector<int>>& grid) {
       int n=grid.size();
       int m=grid[0].size();
       queue<pair<pair<int,int>,int>> q;//位置，腐烂的分钟
        int fresh=0;
       for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                //把腐烂橘子加入队列，并统计新鲜句子数量
                if(grid[i][j]==2){
                    q.push({{i,j},0});
                }
                else if(grid[i][j]==1){
                    fresh++;
                }
            }
       }
        int max_ans=0;
       while(!q.empty()){
            auto tmp=q.front();
            q.pop();
            int x=tmp.first.first;
            int y=tmp.first.second;
            int t=tmp.second;//位置 时间
            max_ans=max(max_ans,t);

            for(int i=0;i<4;i++){
                int new_x=x+dx[i];
                int new_y=y+dy[i];
                if(new_x>=0&&new_y>=0&&new_x<n&&new_y<m&&grid[new_x][new_y]==1){
                    grid[new_x][new_y]=2;//让他腐烂！！！！！
                    q.push({{new_x,new_y},t+1});
                    fresh--;
                }
                    
            }
       }
       if(fresh==0) return max_ans;
       else return -1;
    }
};

```



### 1765. 地图中的最高点

[1765. 地图中的最高点 - 力扣（LeetCode）](https://leetcode.cn/problems/map-of-highest-peak/description/)

✅ 给你一个大小为 `m x n` 的整数矩阵 `isWater` ，它代表了一个由 **陆地** 和 **水域** 单元格组成的地图。

- 如果 `isWater[i][j] == 0` ，格子 `(i, j)` 是一个 **陆地** 格子。
- 如果 `isWater[i][j] == 1` ，格子 `(i, j)` 是一个 **水域** 格子。

你需要按照如下规则给每个单元格安排高度：

- 每个格子的高度都必须是非负的。
- 如果一个格子是 **水域** ，那么它的高度必须为 `0` 。
- 任意相邻的格子高度差 **至多** 为 `1` 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）

找到一种安排高度的方案，使得矩阵中的最高高度值 **最大** 。

请你返回一个大小为 `m x n` 的整数矩阵 `height` ，其中 `height[i][j]` 是格子 `(i, j)` 的高度。如果有多种解法，请返回 **任意一个** 。



✒️ 一定要记住初始化，力扣函数里的都是局部变量

vector的初始化 指定大小

```c++
vector<vector<int>> a(5,vector<int> (10))//5行10列 初始化为0
vector<vector<int>> a(5,vector<int> (10,-1))//5行10列 初始化为-1
```

一维

```c++
vector<int> v(5, 10);//大小为5 初始化为10
```



如果出现超时报错，大概率是陷入死循环了，没有标记

```c++
class Solution {
private:
    int dx[4]={0,1,0,-1};
    int dy[4]={1,0,-1,0};
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        
        queue<pair<pair<int,int>,int>> q;//位置 水位
        int n=isWater.size();
        int m=isWater[0].size();
        vector<vector<int>> ans=isWater;//没有初始化

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                //找到所有水域 并加入队列
                if(isWater[i][j]==1){
                    q.push({{i,j},0});//高度一定为0
                    ans[i][j]=0;
                }
            }
        }

        while(!q.empty()){
            auto tmp=q.front();
            q.pop();
            int x=tmp.first.first;
            int y=tmp.first.second;
            int h=tmp.second;

            for(int k=0;k<4;k++){
                int n_x=x+dx[k];
                int n_y=y+dy[k];
                if(n_x>=0&&n_y>=0&&n_x<n&&n_y<m&&isWater[n_x][n_y]==0){
                    isWater[n_x][n_y]=1;
                    ans[n_x][n_y]=h+1;
                    q.push({{n_x,n_y},h+1});
                }
            }
        }
        return ans;


    }
};
```

