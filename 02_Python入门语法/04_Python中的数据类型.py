#
print(type(3))
print(type(3.14))
print(type("圆周率"))
#
print("\f")
string_type=type("圆周率")
print(string_type)#查询变量存储的数据的类型
print(type(string_type))
#
print("\f")
t = type(3)      # 不要用 type 当变量名，会覆盖内置函数 type
t2 = t
print(t2)
print("\n")
x = 10          # x 指向一个 int 对象
print(type(x))  # <class 'int'>  ← 这是「10」的类型，不是 x 的类型
x = "十"        # 同一个 x 改指向 str 对象
print(type(x))  # <class 'str'>