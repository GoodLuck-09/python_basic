# 解包：将一个序列的值解包放在不同的变量中
values = [1, 2, 3]
x, y, z = values
print(x, y, z)


# 可以使用 * 收集多余的值
values_other = [1, 2, 3, 4]
a, *b, c = values_other
print(a, b, c)

# 解包之后的多余的值是一个列表


