class Solution:
    def countAndSay(self, n: int) -> str:
        def cas(n):
            if n == 1:
                return "1"
            else:
                prev_res = cas(n-1)
                res = ""
                count = 1
                for i in range(len(prev_res)-1):
                    if prev_res[i] == prev_res[i+1]:
                        count += 1
                    else:
                        res += str(count)+prev_res[i]
                        count = 1
                res += str(count) + prev_res[-1]
                return res
        return cas(n)