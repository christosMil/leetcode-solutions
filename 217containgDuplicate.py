def containsDuplicate(nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

integer_array = [1,2,3,4,2334,545,432,4523,45,4325]
print(integer_array)
print(containsDuplicate(integer_array))
