def moveZeroes(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        terminate_loop = len(nums)
        i = 0
        while i < terminate_loop:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                terminate_loop -= 1
            else:
                i += 1

nums = [0,1,0,3,12]
print(nums)
moveZeroes(nums)
print(nums)
