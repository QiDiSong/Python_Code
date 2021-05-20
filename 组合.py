class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def traceBack(n, k, begin):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(begin, n+1):
                path.append(i)
                traceBack(n, k, i + 1)
                path.pop()
        traceBack(n, k, 1)
        return ans
