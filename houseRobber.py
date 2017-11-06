def houseRobber(nums):
    if not nums:
        return 0

    nlen = len(nums)
    if nlen<=2:
        return max(nums)

    # O(n) time, O(1) space
    prev = max(nums[2] + nums[0], nums[1])
    prev2 = nums[1]
    prev3 = nums[0]
    for i in range(3,nlen):
        current = max(nums[i] + prev2, nums[i] + prev3, prev)
        prev3 = prev2
        prev2 = prev
        prev = current

    return max(prev, prev2)    
    
    '''
    # O(n) time and space
    profit = [0] * nlen # max profit if using that indexed value
    profit = nums[0:2]
    profit.append(max(nums[2] + profit[0], profit[1])) 

    for i in range(3,nlen):
        profit.append(max(nums[i] + profit[i-2], nums[i] + profit[i-3], profit[i-1]))

    return max(profit[nlen-1], profit[nlen-2])
    '''
    #return max(nums[0] + houseRobber(nums[2:]), houseRobber(nums[1:]))

houseValues = [4, 1, 2, 7, 5, 3, 1] # 14
print(houseRobber(houseValues))

houseValues = [2, 1]
print(houseRobber(houseValues))

houseValues = [1, 1, 1]
print(houseRobber(houseValues))

houseValues = [2, 4, 2]
print(houseRobber(houseValues))

houseValues = [2, 1, 1, 1]
print(houseRobber(houseValues))

houseValues = [1, 7, 9, 4]
print(houseRobber(houseValues))

