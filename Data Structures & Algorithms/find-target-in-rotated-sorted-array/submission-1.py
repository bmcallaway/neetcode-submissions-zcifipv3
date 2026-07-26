class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        smallestIdx = 0
        m = 0
        while l <= r:
            m = math.floor((r+l)/2)
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else: 
                smallestIdx = m
                break

        list1, list2 = nums[0:m], nums[m:len(nums)]

        l, r = 0, len(list1)-1
        while l <= r:
            m = math.floor((r+l) / 2)
            if list1[m] > target:
                r = m - 1
            elif list1[m] < target:
                l = m + 1
            elif list1[m] == target:
                return m
        
        l, r = 0, len(list2)-1
        while l <= r:
            m = math.floor((r+l) / 2)
            if list2[m] > target:
                r = m - 1
            elif list2[m] < target:
                l = m + 1
            elif list2[m] == target:
                return m + smallestIdx

        return -1

        