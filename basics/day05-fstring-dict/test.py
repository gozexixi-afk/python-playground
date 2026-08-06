#代码阅读
pi = 3.14159265
total = 9876543
name = "Python"

print(f"{pi:.3f}")                    # 输出 A 3.141
#保留 3 位小数，四舍五入！！！ 3.142
print(f"{total:,}")                   # 输出 B 9，876，543
print(f"{name:>10}|")                 # 输出 C Python     |
#    Python|   ← >10 右对齐占 10 位 对齐的是文字！
print(f"{pi + 1 = :.2f}")            # pi+1 = 4.14输出 D（Python 3.8+）

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_a = [n * 3 for n in numbers if n % 3 == 0]
result_b = [n if n % 2 == 0 else -n for n in numbers[:5]]
result_c = {n: n**2 for n in range(1, 6) if n % 2 != 0}
result_d = sum(1 for n in numbers if n > 5)

print(result_a)  # 输出 A [3,6,9]
print(result_b)  # 输出 B [-1,2,-3,4,-5]
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
print(swapped[2])               # 输出 D 3：“b”

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
## 推导式的优势是可读性更好 列表推导式是python特有语法
## 列表推导式性能稍好，简单逻辑用列表推导式，复杂逻辑用循环

# `dict[key]` 和 `dict.get(key, default)` 有什么区别？
# key不存在于dict时dict[key]会报错  KeyError
# 在什么场景下必须用 `.get()`？不确定key是否存在于dict时
## 处理 API 返回的数据

# ！！！
# Python 有 `%` 格式化、`.format()`、f-string 三种字符串格式化方式，
# 它们的优缺点分别是什么？为什么现在推荐 f-string？
## %最老的写法，不直观易出错
## .format()支持位置参数和命名参数，但是啰嗦
## f-string直观 性能好（编译时处理）支持多行


#实战编程
api_response = {
    "data": {
        "articles": [
            {"id": 1, "title": "Python 入门", "tags": ["python", "beginner"], "views": 1500},
            {"id": 2, "title": "FastAPI 教程", "tags": ["python", "web", "api"], "views": 3200},
            {"id": 3, "title": "Vue 3 指南", "tags": ["javascript", "frontend"], "views": 2800},
            {"id": 4, "title": "Docker 基础", "tags": ["devops", "docker"], "views": 900},
            {"id": 5, "title": "Python 进阶", "tags": ["python", "advanced"], "views": 4100},
        ]
    }
}

articles = api_response["data"]["articles"]

# 任务 1：提取所有 Python 相关文章的标题（用推导式）
py_title = [article["title"] for article in articles if "python" in article["tags"]]
# 任务 2：计算所有文章的平均浏览量
ave_view = sum(article["views"] for article in articles)/len(articles)
# 任务 3：按浏览量排序，输出 Top 3
view_sorted = sorted(articles, key=lambda article: article["views"], reverse=True)[:3]
# 任务 4：统计所有出现过的 tag 及其出现次数
from collections import Counter
#tag_counts = Counter(article["tags"] for article in articles)
## 列表不是可迭代对象，列表是不可哈希的，不能作为 Counter 的 key，直接报错。
# 把嵌套的tags列表打平，取出每一个tag字符串
all_tags = [tag for article in articles for tag in article["tags"]]
tag_counts = Counter(all_tags)
# print(tag_counts)
all_tags_gen = (tag for article in articles for tag in article["tags"])
tag_counts = Counter(all_tags_gen)

# 任务 5：用 f-string 格式化输出报告
# report = f"""
# -----统计报告----
# Python 相关文章的标题：{py_title}
# 文章的平均浏览量：{ave_view}
# 浏览量Top 3:{view_sorted}
# tag及其出现次数:{tag_counts}
# """
# print(report)
print(f"""
=== 文章统计报告 ===
总文章数：{len(articles)}
平均浏览：{ave_view:,.0f}
Python 相关：{len(py_title)} 篇

Top 3 热门文章：
""" + "\n".join([###每条排行字符串用换行符拼接
    f"  {i+1}. {a['title']} ({a['views']:,} 次浏览)"
    for i, a in enumerate(view_sorted)
]) + f"""

热门标签：{', '.join(f'{tag}({count})' for tag, count in tag_counts.most_common(5))}
""")


def build_rag_prompt(
    question: str,
    documents: list[dict],   # [{"text": "...", "source": "...", "score": 0.95}, ...]
    min_score: float = 0.7,
    max_context_length: int = 1000,
) -> str:
    """
    构造 RAG Prompt：
    1. 过滤掉 score < min_score 的文档
    2. 按 score 从高到低排序
    3. 拼接上下文（不超过 max_context_length 字符）
    4. 用多行 f-string 构造完整 Prompt
    """
    # 你的代码
    # #过滤掉 score < min_score 的文档
    # low_score = [document for document in documents if document["score"] < min_score]
    # #按 score 从高到低排序
    # score_sorted = sorted(low_score,key = lambda d : d["score"],reverse=True)
    # #拼接上下文（不超过 max_context_length 字符）
    # text_com = [document["text"] for document in documents if len(document["text"])<max_context_length]
    # #用多行 f-string 构造完整 Prompt
    # prompt = f"""
    # 参考文档：{low_score}
    # 文档关联度排序（高到低）：{score_sorted}
    # 回答{text_com}
    # """
    # return prompt
    # 1. 过滤 + 排序
    relevant = sorted(
        [d for d in documents if d["score"] >= min_score],
        key=lambda d: d["score"],
        reverse=True
    )

    # 2. 拼接上下文（控制长度）
    context_parts = []
    total_length = 0
    for doc in relevant:
        line = f"[来源: {doc['source']}] {doc['text']}"
        if total_length + len(line) > max_context_length:
            break
        context_parts.append(line)
        total_length += len(line)

    context = "\n    ".join(context_parts) if context_parts else "（没有相关文档）"

    # 3. 构造 Prompt
    return f"""你是一个知识助手。请仅根据以下参考文档回答用户问题。

    ## 规则
    - 只使用参考文档中的信息
    - 如果文档中没有答案，请说"根据现有资料无法回答"
    - 回答简洁，不超过 200 字

    ## 参考文档
    {context}

    ## 用户问题
    {question}"""


# 测试
docs = [
    {"text": "Python 是 Guido van Rossum 创建的编程语言。", "source": "wiki", "score": 0.95},
    {"text": "Python 支持面向对象和函数式编程。", "source": "wiki", "score": 0.88},
    {"text": "Java 是另一种流行的编程语言。", "source": "wiki", "score": 0.45},
    {"text": "Python 的包管理器是 pip。", "source": "docs", "score": 0.82},
]

prompt = build_rag_prompt("Python 有哪些特点？", docs)
print(prompt)