# import requests
#
# print(requests.__version__)  # 能打印版本号就说明装好了
# print("---------------")
# # 向 JSONPlaceholder（一个专门用来练习的假 API）发请求
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#
# # 看看返回了什么
# print(response.status_code)  # 200 = 成功，404 = 找不到，500 = 服务器炸了
# print(response.text)         # 返回的原始文本（JSON 字符串）
# print(response.text["title"])
# # 调一个随机名言 API（原 api.quotable.io 证书过期，换成 zenquotes）
# response = requests.get("https://zenquotes.io/api/random")
# print(f"状态码：{response.status_code}")
# print(f"返回类型：{type(response.json())}")
#
# data = response.json()[0]
# print(f"名言：{data['q']}")
# print(f"作者：{data['a']}")

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.text)
# 方法一：手动用 json 模块转换
data = json.loads(response.text)   # loads = load string → 把字符串解析成字典
print(type(data))                  # <class 'dict'>
print(data["body"])               # 现在可以像字典一样取值了

# 方法二（推荐）：requests 自带的快捷方法
data = response.json()             # 效果一样，内部帮你做了 json.loads
print(data["title"])