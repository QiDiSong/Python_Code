'''
664. 奇怪的打印机
有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

示例 1：
输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。

示例 2：
输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
'''
class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    _min = sys.maxsize
                    for k in range(i, j):
                        _min = min(_min, dp[i][k] + dp[k+1][j])
                    dp[i][j] = _min
        return dp[0][len(s)-1]
        
        
'''
方法一：动态规划
思路及算法

我们可以使用动态规划解决本题，令 f[i][j]f[i][j] 表示打印完成区间 [i,j][i,j] 的最少操作数。

当我们尝试计算出 f[i][j]f[i][j] 时，需要考虑两种情况：

s[i]=s[j]s[i]=s[j]，即区间两端的字符相同，那么当我们打印左侧字符 s[i]s[i] 时，可以顺便打印右侧字符 s[j]s[j]，这样我们即可忽略右侧字符对该区间的影响，只需要考虑如何尽快打印完区间 [i,j-1][i,j−1] 即可，即此时有 f[i][j]=f[i][j-1]f[i][j]=f[i][j−1]。
我们无需关心区间 [i,j-1][i,j−1] 的具体打印方案，因为我们总可以第一步完成 s[i]s[i] 的打印，此时可以顺便完成 s[j]s[j] 的打印，不会影响打印完成区间 [i,j-1][i,j−1] 的最少操作数。
s[i] \neq s[j]s[i] 

​	
 =s[j]，即区间两端的字符不同，那么我们需要分别完成该区间的左右两部分的打印。我们记两部分分别为区间 [i,k][i,k] 和区间 [k+1,j][k+1,j]（其中 i \leq k < ji≤k<j），此时 f[i][j]=\min_{k=i}^{j-1}{f[i][k]+f[k+1][j]}f[i][j]=min 
k=i
j−1
​	
 f[i][k]+f[k+1][j]。
总结状态转移方程为：

f[i][j] = \begin{cases} f[i][j-1],& s[i]=s[j] \\ \min_{k=i}^{j-1}{f[i][k]+f[k+1][j]},& s[i]\neq s[j] \end{cases}
f[i][j]={ 
f[i][j−1],
min 
k=i
j−1
​	
 f[i][k]+f[k+1][j],
​	
  
s[i]=s[j]
s[i] 

​	
 =s[j]
​	
 

边界条件为 f[i][i]=1f[i][i]=1，对于长度为 11 的区间，需要打印 11 次。最后的答案为 f[0][n-1]f[0][n−1]。

注意到 f[i][j]f[i][j] 的计算需要用到 f[i][k]f[i][k] 和 f[k+1][j]f[k+1][j]（其中 i\leq k< ji≤k<j）。
为了保证动态规划的计算过程满足无后效性，在实际代码中，我们需要改变动态规划的计算顺序，从大到小地枚举 ii，并从小到大地枚举 jj，
这样可以保证当计算 f[i][j]f[i][j] 时，f[i][k]f[i][k] 和 f[k+1][j]f[k+1][j] 都已经被计算过。

'''
