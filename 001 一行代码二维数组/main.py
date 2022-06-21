# 生成了十行六列的二维数组
arr = [[0] * 6 for _ in range(10)]

# 注意点：最内层可以用乘号，但是外层就要用 xxx for _ in range(???) 来复制了
# 因为  乘法展开 是用的同一块内存地址
# 之所以最内层是可以用乘法的，因为python里的小整数都是共用的同一个内存，所有的0 1,2 3 …… 都是同一个内存地址
a = 1
b = 1
c = 1
print(id(a), id(b), id(c))
# 140718669554512 140718669554512 140718669554512
print(a is b is c)
for i in range(-10000, 100000):
    s = f"n1 = {i}\n"
    s += f"n2 = {i}\n"
    s += "print(i, n1 is n2)"
    exec(s)

# 结果居然全是True
# 底层机制还有待研究
