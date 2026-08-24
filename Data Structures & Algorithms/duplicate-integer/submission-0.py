class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicated=[]
        for i in range(len(nums)):
            if(nums[i]  in duplicated):
                return True
            duplicated.append(nums[i])
        return False