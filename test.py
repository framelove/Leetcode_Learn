class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None: return []
        if len(nums) == 1: return [nums]
        res = []
        for x in nums:
            ys = nums + []
            ys.remove(x)
            for y in self.permute(ys):
                res.append([x] + y)
        return res

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(res, l, r, n, max):
            if n == max:
                print(l)
                res.append(l)
            for i in range(0, len(r)):
                helper(res, l + [r[i]], r[:i] + r[i + 1:], n + 1, max)

        helper(res, [], nums, 0, len(nums))
        return res

a = [1,2]
q = Solution()
print(q.permute1(a))

