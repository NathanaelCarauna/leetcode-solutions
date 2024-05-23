class Solution(object):
    def longestCommonPrefix(self, strs):
        answer = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return answer
            answer += first[i]
        return answer
        