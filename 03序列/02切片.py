"""
    切片
        切片指从现有列表中，获取一个子列表
        通过切片来获取指定的元素
    语法：
        列表[起始:结束]

        通过切片获取元素时，会包括起始位置的元素，不会包括结束位置的元素
        做切片操作时，总会返回一个新的列表，不会影响原来的列表
        起始和结束位置的索引都可以省略不写
        如果省略结束位置，则会一直截取到最后。例如：stus[1:]
        如果省略起始位置，则会从第一个元素开始截取。例如：stus[:3]
        如果省略起始和结束位置，则相当于创建一个列表的副本。例如：stus[:]

        列表[起始:结束:步长]

        步长表示，每次获取元素的间隔，默认值是1
        步长不能是0，但可以是负数
        如果是负数，则会从列表的后部向前边取元素
        stus[::-1]

    列表的索引可以是负数
        如果索引是负数，则从后向前获取元素，-1表示倒数第一个，-2表示倒数第二个，以此类推

    通过切片修改列表
        在给切片赋值时，只能使用序列
        在设置步长时，序列中元素的个数必须和切片中元素的个数一致

    通过切片删除列表元素

"""

# 创建列表
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']

# 使用索引获取倒数第二个元素
print(stus[-2])

# 使用切片获取数据，从第一个开始向后获取全部元素
print(stus[1:])
# 从第一个元素开始获取到第三个元素，不包含第三个元素
print(stus[1:3])
# 从第一个开始获取到第三个，间隔为2
print(stus[1:3:2])
# 从后部向前获取元素
print(stus[::-1])

# 通过切片修改元素
stus[0:2] = ['牛魔王','红孩儿']
# 设置步长,序列中元素个数必须和切片中元素个数一致
stus[::2] = ['牛魔王','红孩儿','二郎神']
print(stus)

# 通过切片删除元素
del stus[0:2]   # 删除第一个和第二个元素
del stus[::2]   # 从第0个开始删除，间隔2删除一个
stus[1:3] = []  # 删除第一个和第二个

print(stus)


