nums = [1,2,3]
i_nums = nums.__iter__()
i_nums1=iter(nums)
#print(dir(nums))

print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
#iterable if has __iter__

#iterator- object with aa state where it remembers state during iteration
#__next__ and __state__

