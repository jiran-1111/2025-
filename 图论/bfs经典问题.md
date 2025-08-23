## bfs经典问题–序号

**207 210** 

## 题目

### 207. 课程表①

✅你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程 `bi` 。

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。



[207. 课程表 - 力扣（LeetCode）](https://leetcode.cn/problems/course-schedule/?envType=study-plan-v2&envId=top-100-liked)

这也是一道bfs题目，来实现拓扑排序，本质也是一种遍历问题的剪枝

我们可以将课程看作图中的节点，先修课程看作图中的边，那么我们可以将本题转化为判断**有向图中是否存在环**。

具体地，我们可以使用拓扑排序的思想，对于每个入度为 0 的节点，我们将其出度的节点的入度减 1，直到所有节点都被遍历到。

如果所有节点都被遍历到，说明图中不存在环，那么我们就可以完成所有课程的学习；否则，我们就无法完成所有课程的学习。



很巧妙的使用**入度数的数组**，这样可以很大程度上避免在矩阵中纵向遍历的时间复杂度的飙升

为什么我就想不到……



```c++
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(numCourses);
        vector<int> indeg(numCourses);
        for (auto& p : prerequisites) {//也是二维数组 
            int a = p[0], b = p[1];
            g[b].push_back(a);//第二个指向第一个 
            ++indeg[a];//记录入度数量
        }

        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {//把入度数为0的点先放入栈中
                q.push(i);
            }
        }
        //cnt记录出栈的个数 每次都把栈顶元素pop掉
        int cnt = 0;
        //把每个入度为空点连接的边都删掉 指向的点的入度都减去1
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            ++cnt;
            for (int j : g[i]) {//j表示入度为空的点所指向的点
                if (--indeg[j] == 0) {//这些点-- 如果等于0 则入栈 这里很巧妙 不用再for循环进行判断了
                    q.push(j);
                }
            }
        }
        return cnt == numCourses;
    }
};


```

***时间复杂度 O(n+m)***



### 210.课程表②

[210. 课程表 II - 力扣（LeetCode）](https://leetcode.cn/problems/course-schedule-ii/description/)

和上面那道题一样的做法，把数组输出了而已

```c++
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ans(numCourses);
        vector<int> fal;
        vector<vector<int>> g(numCourses);
        vector<int> indeg(numCourses);
        for (auto& p : prerequisites) {//也是二维数组 
            int a = p[0], b = p[1];
            g[b].push_back(a);//第二个指向第一个 
            ++indeg[a];//记录入度数量
        }

        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) {//把入度数为0的点先放入栈中
                q.push(i);
            }
        }
        //cnt记录出栈的个数 每次都把栈顶元素pop掉
        int cnt = 0;
        int k=0;
        //把每个入度为空点连接的边都删掉 指向的点的入度都减去1
        while (!q.empty()) {
            int i = q.front();
            ans[k++]=i;
            q.pop();
            ++cnt;
            for (int j : g[i]) {//j表示入度为空的点所指向的点
                if (--indeg[j] == 0) {//这些点-- 如果等于0 则入栈 这里很巧妙 不用再for循环进行判断了
                    q.push(j);
                }
            }
        }
        if (cnt == numCourses) return ans;
        else return fal;
    }
};
```

