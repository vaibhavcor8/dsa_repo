class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(findFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if findFirst:
                        right = mid - 1 # Look left
                    else:
                        left = mid + 1  # Look right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound
        
        return [findBound(True), findBound(False)]
    
    # first commit