import string
#P1-1
# 代码阅读题
# 输出是赋值的是地址 [1,2,3,4],true
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b is a)
print("------------------")
# 输出是{"a": 10, "b": 2,"c" : 1}
d = {"a": 1, "b": 2}
d["a"] = 10
d["c"] = d.get("c", 0) + 1
print(d)
# 输出是4 <class 'set'>
#为什么 `len(s)` 不是 6:因为s不是值可重复的dict，是不可重复的set集合
s = {1, 2, 3, 2, 1, 4}
print(len(s))
print(type(s))
# 代码纠错题
# 想统计列表中每个元素的出现次数，但会报错。找出并修复
# items = ["apple", "banana", "apple", "cherry"]
# counts = {}
# for item in items:
#     counts[item] = counts[item] + 1 得判断是否存在这个key
# print(counts)
items = ["apple", "banana", "apple", "cherry"]
counts = {}
for item in items:
    counts[item]=counts.get(item,0) + 1
print(counts)
# 想遍历字典筛选高分学生，但运行报错。找出并修复
# scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
# top_students = []
# for name, score in scores:遍历有问题
#     if score > 80:
#         top_students.append(name)
# print(top_students)
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
top_students = []
for name, score in scores.items():
    if score > 80:
        top_students.append(name)
print(top_students)
# 面试八股题
# 以下哪些操作的时间复杂度是 O(1)？（多选）AC
# A. `list.append(x)`
# B. `list.insert(0, x)`所有原有元素都要向后移位
# C. `dict[key]`（查找）字典基于哈希表实现，通过哈希值直接定位存储位置
# D. `x in list`（查找）列表无哈希索引，需要从头到尾逐个对比元素

# !!!Python的dict和JavaScript的Object有什么主要区别？至少说 2 点。
# object中key只能为string/symbol dict为任意
# object有原型链问题
# object遍历/求长度都需先转为数组，dict for...of/size（）
# 所有对象都为true 空字典为空

#实战编程题
# 写一个函数 `count_words_top(text: str, top_n: int = 3)
# -> list[tuple]`，统计文本中出现次数最多的前 N 个单词（忽略大小写），返回 `[(word, count), ...]`
def count_words_top(text: str, top_n: int = 3) -> list[tuple]:
    words = text.lower().split()
    words_count = {}
    more_words : list[tuple] = []
    for word in words:
        words_count[word] = words_count.get(word,0) + 1
    print(words_count)
    for word, count in words_count.items():
        more_words.append( (word, count) )
    print(more_words)
    return more_words[:top_n ]

print(count_words_top("Hello hello World world world Python python Python python! Hello, Python", 3))