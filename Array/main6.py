def __init__(self, nums):
    self.prefix = [0]
    
    for num in nums:
        self.prefix.append(self.prefix[-1] + num)
    
def sumRange(self, i, j):
    return self.prefix[j + 1] - self.prefix[i]
