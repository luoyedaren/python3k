from functools import reduce


def normalize(args):
    return str(args[0:1]).upper() + str(args[1:]).lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print("----------------------------")


def prod(param):
    return reduce(lambda x, y: x * y, param)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
