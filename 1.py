class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict = {}
        res = []

        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1

        pos = [i for i in num_dict if i > 0]
        neg = [i for i in num_dict if i < 0]
        neg.sort()
        # 特殊情况的妙用
        if 0 in num_dict and num_dict[0] >= 3:
            res.append([0, 0, 0])
        for i in pos:
            for j in neg:
                # a+b+c = 0
                # a+b = -c
                k = -i - j
                if k in num_dict:
                    if (k == i or k == j) and num_dict[k] >= 2:
                        res.append([j, k, i])
                    elif j < k < i:
                        res.append([j, k, i])
                    if k < j:
                        break
        return res

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None





ids = [1,0,1,1,2]
a = Solution()
print(a.twoSum(ids,2))
