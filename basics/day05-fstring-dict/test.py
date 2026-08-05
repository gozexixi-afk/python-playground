#代码阅读
pi = 3.14159265
total = 9876543
name = "Python"

print(f"{pi:.3f}")                    # 输出 A 3.141
print(f"{total:,}")                   # 输出 B 9，876，543
print(f"{name:>10}|")                 # 输出 C Python     |
print(f"{pi + 1 = :.2f}")            # pi = 4.14输出 D（Python 3.8+）

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_a = [n * 3 for n in numbers if n % 3 == 0]
result_b = [n if n % 2 == 0 else -n for n in numbers[:5]]
result_c = {n: n**2 for n in range(1, 6) if n % 2 != 0}
result_d = sum(1 for n in numbers if n > 5)

print(result_a)  # 输出 A [3,6,9]
print(result_b)  # 输出 B [-1,2,-3,4]
print(result_c)  # 输出 C {1：1，3：9，5：25}
print(result_d)  # 输出 D 5

defaults = {"theme": "light", "lang": "zh", "size": 14}
custom = {"lang": "en", "size": 16, "bold": True}

merged = defaults | custom
print(merged["lang"])           # 输出 A en
print(merged.get("theme"))      # 输出 B light
print(len(merged))              # 输出 C 4

d = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in d.items()}
print(swapped[2])               # 输出 D 3：“c”

#代码纠错
# 目标：提取所有价格大于 100 的商品名称
products = [
    {"name": "键盘", "price": 199},
    {"name": "鼠标", "price": 79},
    {"name": "显示器", "price": 1299},
    {"name": "耳机", "price": 149},
]

expensive = [product["name"] for product in products if product["price"] > 100 ]
print(expensive)
# 期望输出：['键盘', '显示器', '耳机']
# 实际输出正确，但代码有一个逻辑问题——它不应该检查 name

base = {"host": "localhost", "port": 8000, "debug": False}
override = {"port": 3000, "debug": True}

# 目标：让 override 覆盖 base 的值
# result = override | base
result = base | override
print(result["port"])   # 期望 3000，实际输出 8000

#面试八股
# ！！！
# 列表推导式和 `map()` + `filter()` 有什么区别？
# 什么时候用推导式，什么时候用循环？
#列表推导式可以用一行代码完成`map()` + `filter()`的操作

# `dict[key]` 和 `dict.get(key, default)` 有什么区别？
# key不存在于dict时dict[key]会报错
# 在什么场景下必须用 `.get()`？不确定key是否存在于dict时

# ！！！
# Python 有 `%` 格式化、`.format()`、f-string 三种字符串格式化方式，、
# 它们的优缺点分别是什么？为什么现在推荐 f-string？
