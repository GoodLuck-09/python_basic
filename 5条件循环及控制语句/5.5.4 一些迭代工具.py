# 并行迭代

names = ['anne', 'beth', 'geogre', 'damon']
ages = [1, 2, 3, 4]

new_li = list(zip(names, ages))
print(new_li)
new_d = dict(zip(names, ages))
print(new_d)

# enumerate 迭代时获取索引
for index, string in enumerate(names):
    print(index, string)

# sorted, reversed
new_ages = sorted(ages)
print(new_ages)

# sort函数没有返回值
number = [1, 2, 4, 3]
number.sort()
print(number)