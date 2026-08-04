import requests


def fetch_weather(city: str, api_key: str) -> dict | None:
    """
    安全地获取天气数据，处理所有可能的失败场景。
    返回 None 表示失败。
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "zh_cn"}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # 4xx/5xx 状态码会抛出 HTTPError
        return response.json()

    except requests.exceptions.Timeout:
        print(f"[超时] 服务器 5 秒内没有响应")
    except requests.exceptions.ConnectionError:
        print(f"[连接失败] 请检查网络连接")
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        if status == 401:
            print(f"[认证失败] API Key 无效或已过期")
        elif status == 404:
            print(f"[未找到] 城市 '{city}' 不存在")
        elif status == 429:
            print(f"[限流] 请求太频繁，请稍后再试")
        else:
            print(f"[HTTP 错误 {status}] {e}")
    except ValueError:
        print(f"[解析错误] 服务器返回的不是有效 JSON")
    except Exception as e:
        print(f"[未知错误] {type(e).__name__}: {e}")

    return None

# 测试各种场景
result = fetch_weather("Hangzhou", "你的key")  # 正常
result = fetch_weather("不存在的地方xyz", "你的key")  # 404
result = fetch_weather("Hangzhou", "错误的key")       # 401

# 写文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行：你好 Python\n")
    f.write("第二行：文件操作很简单\n")
    f.write("第三行：with 自动关闭文件\n")

# 读文件（全部内容）
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("--- 全部内容 ---")
    print(content)

# 逐行读取（大文件推荐）
with open("test.txt", "r", encoding="utf-8") as f:
    print("--- 逐行读取 ---")
    for line in f:
        print(f"  | {line.strip()}")  # strip() 去掉末尾的换行符

# 追加内容
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("第四行：这是追加的内容\n")

# 验证追加成功
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 返回所有行的列表
    print(f"共 {len(lines)} 行")
    for i, line in enumerate(lines, 1):
        print(f"  行{i}: {line.strip()}")

import json

# 写入 JSON 文件
conversations = [
    {"role": "user", "content": "什么是 Python？", "time": "2026-08-03T10:00:00"},
    {"role": "assistant", "content": "Python 是一种编程语言...", "time": "2026-08-03T10:00:02"},
    {"role": "user", "content": "怎么学 Python？", "time": "2026-08-03T10:01:00"},
]

with open("history.json", "w", encoding="utf-8") as f:
    json.dump(conversations, f, ensure_ascii=False, indent=2)
    # ensure_ascii=False → 中文不被转义（不写的话 "你好" 变成 "\u4f60\u597d"）
    # indent=2 → 格式化缩进（不写的话全挤在一行）

# 读取 JSON 文件
with open("history.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"共 {len(loaded)} 条对话")
for msg in loaded:
    print(f"  [{msg['time'][:16]}] {msg['role']}: {msg['content'][:30]}...")

import json

# dump/load 操作文件
data = {"name": "周佳", "skills": ["Vue", "Python"]}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("user.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)  # 返回 dict

# dumps/loads 操作字符串
json_string = json.dumps(data, ensure_ascii=False)
print(json_string)  # {"name": "周佳", "skills": ["Vue", "Python"]}

parsed = json.loads(json_string)  # 返回 dict
print(parsed["name"])  # "周佳"