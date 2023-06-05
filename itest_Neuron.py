def moveZeroes(nums):
    left = right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    for i in range(left, len(nums)):
        nums[i] = 0

    return nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
