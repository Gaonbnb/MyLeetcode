def helper(res, nums, list_, index):

    if index == len(nums):
        res = res.append(list_)
        return            
    helper(res, nums, list_, index+1)
    #list_ = list_ + [nums[index]] 
    list_.append(nums[index]) 
    #list_ += [nums[index]] #错误写法，id不变
    
    helper(res, nums, list_, index+1)
    
    list_.pop()
nums = [1, 2, 3]
res = list()
list_ = []
helper(res, nums, list_, 0)
print(res)