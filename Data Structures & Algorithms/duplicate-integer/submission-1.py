class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        viewed =[]
        for num in nums:
            if num in viewed:
                return True
            viewed.append(num)
        return False