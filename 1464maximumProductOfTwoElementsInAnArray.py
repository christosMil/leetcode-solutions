def maxProduct(nums: list) -> int:
        nums.sort()
        return (nums[len(nums)-1] - 1)*(nums[len(nums)-2] - 1)

nums = [3,4,5,2]
print(nums, maxProduct(nums))
