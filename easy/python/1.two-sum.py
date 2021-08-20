def twoSum(nums: list[int], target: int) -> list[int]:
    
    answers = []

    i = 0
    while (i < len(nums)-1):
        z = i+1
        while (z < len(nums)):
            if (nums[i]+nums[z] == target):
                answers.append(i)
    
    print(answers)

twoSum([1,2,4], 3)