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

########################### 下面这种应用class之外的变量就当作普通的函数和变量的关系去理解，就是局部变量和全局变量的关系
class a:
    numss = [1]
    gao = 1
    def aa(self):
        # print(self.nums) 报错
        global nums
        nums += [1] # 不加global报错
        
        print(nums)
        print(self.numss) # 不加class报错
        self.a = 1
    def bb(self):
        self.a += 1
        print(self.a)
        print(self.gao)
        
aa = a()
aa.aa()
print(nums)
####### self变量的理解，不加aa.aa()就会报错
# aa.bb() # 2
aa.bb() # 3
# a.gao += 100 这里可以看出类变量和实例变量是连接在一起的
aa.bb()


