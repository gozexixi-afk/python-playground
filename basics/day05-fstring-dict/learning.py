import requests


def build_chat_prompt(user_message: str, history: list[dict]) -> str:
    """构造发送给 LLM 的 system prompt"""

    # 用推导式把历史对话格式化成文本（后面模块三会详细讲推导式）
    #"\n".join(...)：把列表里面每一条字符串，用换行符 \n 拼接成一整个大字符串
    history_text = "\n".join([
        f"{msg['role']}: {msg['content']}"
        for msg in history[-4:]  # 只取最近 4 条
    ])

    system_prompt = f"""你是 MemoMind，一个友好的 AI 助手。

## 你的性格
- 回答简洁，通常不超过 3 句话
- 用中文回答
- 如果不确定，诚实地说"我不确定"

## 对话历史
{history_text if history_text else "（暂无历史）"}

## 当前用户消息
{user_message}"""

    return system_prompt


# 测试
history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好！我是 MemoMind。"},
    {"role": "user", "content": "你能做什么？"},
    {"role": "assistant", "content": "我可以回答问题、帮你学习。"},
]

prompt = build_chat_prompt("Python 怎么学？", history)
print(prompt)

# LLM API 的标准返回格式（嵌套字典）
response = {
    "id": "chatcmpl-abc123",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Python 是一门很好的语言！"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 15,
        "total_tokens": 25
    }
}

# 危险写法：一层不存在就 KeyError 崩溃
# content = response["choices"][0]["message"]["content"]

# 安全写法：逐层 .get()
#*keys：可变参数，可以传一串多层的 key / 数组下标
def safe_extract(data: dict, *keys, default=None):
    """安全地从嵌套字典中提取值"""
    #把current当作游标，一层一层往下钻，初始等于最外层字典。
    current = data
    for key in keys:
        #isinstance(变量, 类型)：判断变量是不是字典类型
        if isinstance(current, dict):
            current = current.get(key)
        elif isinstance(current, list) and isinstance(key, int):
            try:
                current = current[key]
            except IndexError:
                return default
        else:
            return default
        if current is None:
            return default
    return current

# 用法
content = safe_extract(response, "choices", 0, "message", "content")
print(content)  # "Python 是一门很好的语言！"

# 不存在的键
missing = safe_extract(response, "choices", 0, "text", default="无内容")
print(missing)  # "无内容"

tokens = safe_extract(response, "usage", "total_tokens")
print(tokens)   # 25

# 统计词频
text = "python is great and python is easy to learn python"
words = text.split()

# 方法 1：手动计数
word_count: dict[str, int] = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'python': 3, 'is': 2, 'great': 1, 'and': 1, 'easy': 1, 'to': 1, 'learn': 1}

# 方法 2：用 Counter（标准库，更优雅）
from collections import Counter
word_count2 = Counter(words)
print(word_count2)
print(word_count2.most_common(3))  # [('python', 3), ('is', 2), ...]
# 模拟 API 返回的用户列表users = [    {"name": "Alice", "age": 28, "active": True, "role": "admin"},    {"name": "Bob", "age": 35, "active": False, "role": "user"},    {"name": "Charlie", "age": 22, "active": True, "role": "user"},    {"name": "Diana", "age": 31, "active": True, "role": "admin"},    {"name": "Eve", "age": 19, "active": True, "role": "user"},]​# 提取所有活跃用户的名字active_names = [u["name"] for u in users if u["active"]]print(active_names)  # ['Alice', 'Charlie', 'Diana', 'Eve']​# 找所有管理员admins = [u for u in users if u["role"] == "admin"]print([a["name"] for a in admins])  # ['Alice', 'Diana']​# 计算平均年龄avg_age = sum(u["age"] for u in users) / len(users)print(f"平均年龄：{avg_age:.1f}")  # 平均年龄：27.0​# 按角色分组from collections import defaultdictby_role = defaultdict(list)for u in users:    by_role[u["role"]].append(u["name"])print(dict(by_role))  # {'admin': ['Alice', 'Diana'], 'user': ['Bob', 'Charlie', 'Eve']}


# 模拟 API 返回的用户列表
users = [
    {"name": "Alice", "age": 28, "active": True, "role": "admin"},
    {"name": "Bob", "age": 35, "active": False, "role": "user"},
    {"name": "Charlie", "age": 22, "active": True, "role": "user"},
    {"name": "Diana", "age": 31, "active": True, "role": "admin"},
    {"name": "Eve", "age": 19, "active": True, "role": "user"},
]

# 提取所有活跃用户的名字
active_names = [u["name"] for u in users if u["active"]]
print(active_names)  # ['Alice', 'Charlie', 'Diana', 'Eve']

# 找所有管理员
admins = [u for u in users if u["role"] == "admin"]
print([a["name"] for a in admins])  # ['Alice', 'Diana']

# 计算平均年龄
avg_age = sum(u["age"] for u in users) / len(users)
print(f"平均年龄：{avg_age:.1f}")  # 平均年龄：27.0

# 按角色分组
from collections import defaultdict
by_role = defaultdict(list)
for u in users:
    by_role[u["role"]].append(u["name"])
print(dict(by_role))  # {'admin': ['Alice', 'Diana'], 'user': ['Bob', 'Charlie', 'Eve']}


# 模拟向量检索返回的结果
search_results = [
    {"text": "Python 是一种编程语言", "similarity": 0.95, "source": "doc1.pdf"},
    {"text": "Python 支持多种编程范式", "similarity": 0.82, "source": "doc1.pdf"},
    {"text": "Java 也是一种编程语言", "similarity": 0.65, "source": "doc2.pdf"},
    {"text": "Python 的语法很简洁", "similarity": 0.78, "source": "doc3.pdf"},
    {"text": "天气预报说明天下雨", "similarity": 0.12, "source": "news.txt"},
]

# 过滤：只保留相似度 > 0.7 的结果
relevant = [r for r in search_results if r["similarity"] > 0.7]
print(f"相关结果：{len(relevant)} 条")

# 提取：只取文本内容
texts = [r["text"] for r in relevant]
print(texts)

# 排序：按相似度从高到低
#lambda r: r["similarity"] 匿名函数
sorted_results = sorted(search_results, key=lambda r: r["similarity"], reverse=True)
for r in sorted_results[:3]:
    print(f"  [{r['similarity']:.2f}] {r['text']}")

# 构造 Prompt 上下文（结合今天的 f-string）
context = "\n".join([
    f"- {r['text']} (来源: {r['source']})"
    for r in relevant
])

prompt = f"""根据以下信息回答问题：

{context}

问题：Python 是什么？"""

print("\n--- Prompt ---")
print(prompt)