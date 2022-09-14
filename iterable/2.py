class MyRange:
    def __init__(self,start,end):
        self.value=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current=self.value
        self.value+=1
        return current

nums = MyRange(1,10)
#either
#for num in nums:
#    print(num)
#or
print(next(nums))
while True:
    try:
        print(next(nums))
    except StopIteration:
        break
