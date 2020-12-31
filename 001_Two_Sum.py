class Solution(object):
    def twoSum(self, nums, target):
        nums_index = [(v,index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums)-1
        while begin<end:
            curr = nums_index[begin][0]+nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr<target:
                begin += 1
            else:
                end-=1

if __name__ == "__main__":
    nums = [2,3,4,5,1,6,7,8,9]
    target = 9
    s = Solution()
    print(s.twoSum(nums,target))
    # for idx, val in enumerate(nums):
    #     print(idx, val)
        