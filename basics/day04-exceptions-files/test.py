#代码阅读题
from sys import path


def process(data: str) -> str:
    try:
        number = int(data)
        result = 100 / number
        return f"结果：{result}"
    except ValueError:
        return "值错误"
    except ZeroDivisionError:
        return "除零错误"
    except Exception as e:
        return f"其他错误：{e}"
    finally:
        print("处理完成")

print(process("10"))     # 输出 A 10 !!!10.0 python中/返回的永远是float
print(process("abc"))    # 输出 B 值错误
print(process("0"))      # 输出 C 除零错误

# 假设 test.txt 内容为 "Hello World"

with open("test.txt", "r", encoding="utf-8") as f:
    line1 = f.read()

print(line1)          # 输出 A Hello World
print(f.closed)       # 输出 B true（？

try:
    print(f.read())   # 输出 C Hello World
    ## ！！！上面的代码关闭了文件，不能进行操作
    #在关闭的文件上调用 `f.read()` 会抛出
    # `ValueError`（I/O operation on closed file）
except Exception as e:
    print(f"错误：{type(e).__name__}")


import json

data = {
    "name": "周佳",
    "skills": ["Vue", "Python"],
    "experience": 1.5
}

# 操作 1
text = json.dumps(data)
print(type(text))            # 输出 A str <class 'str'>

# 操作 2
text2 = json.dumps(data, ensure_ascii=False, indent=2)
print("周佳" in text2)       # 输出 B true

# 操作 3
parsed = json.loads(text)
print(parsed["skills"][0])   # 输出 C
# { “skills” ： “vue”} ！！！vue
print(type(parsed["experience"]))  # 输出 D
#！！！ <class 'float'>     ← JSON 的数字默认解析为 float

#代码纠错题
def save_data(filepath, data):
    # f = open(filepath, "w")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_data(filepath):
    # f = open(filepath, "r")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        return json.loads(content)

import requests
def fetch_and_save(url: str, filepath: str) -> bool:
    try:
        # response = requests.get(url)
        response = requests.get(url, timeout=5)  # 加超时
        response.raise_for_status() #!
        data = response.json()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        #return True
    # except:
    except Exception as e:
        return False
    # else:
    #     return True
#面试八股
# try-》可能有异常的代码
# except-》捕获异常
# else-》没有异常执行
# finally-》不管什么情况都执行

# `with open() as f` 做了什么？打开文件 执行代码 关闭文件
# 为什么比 `f = open()` 更安全？`with` 语句背后的协议是什么？
# with不管有没有执行错误都会关闭文件，当执行f = open（）出现错误，文件可能无法关闭

# `json.dump()` 和 `json.dumps()` 有什么区别？
# dump（data，文件，ensure_ascill,intend）写入json dumps(data)对象-》json字符串
# `ensure_ascii=False` 和 `indent=2` 分别有什么作用？
# 不转义中文， 缩进

def read_json(filepath: str) -> list | dict | None:
    """
    安全读取 JSON 文件。
    - 文件不存在 → 返回 None
    - JSON 格式错误 → 返回 None
    - 成功 → 返回解析后的数据
    """
    # 你的代码
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # data = f.read()
            # data = json.loads(data)！文件用load
            return json.load(f)
    except FileNotFoundError:
        print("文件不存在")
        return None
    # except ValueError:
    except json.JSONDecodeError:
        # print("JSON 格式错误")
        print(f"JSON 格式错误：{filepath}")
        return None
    except Exception as e:
        # print(e)
        print(f"读取失败：{type(e).__name__}: {e}")
        return None
    # else:
    #     return data

def write_json(filepath: str, data: list | dict) -> bool:
    """
    安全写入 JSON 文件。
    - 成功 → 返回 True
    - 任何错误 → 打印错误信息，返回 False
    """
    # 你的代码
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False,indent=2)
    except Exception as e:
        # print(e)
        print(f"写入失败：{type(e).__name__}: {e}")
        return False
    # else:
    #     return True

# 测试
result = read_json("不存在.json")
print(result)  # None

write_json("test.json", [{"name": "周佳"}, {"name": "AI"}])
data = read_json("test.json")
print(data)    # [{'name': '周佳'}, {'name': 'AI'}]
#!!!!!!!
import requests
import time
import json

class SafeAPIClient:
    """健壮的 API 客户端"""

    def __init__(self, base_url: str, timeout: float = 5.0, max_retries: int = 3):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

    def get(self, path: str, params: dict | None = None) -> dict | None:
        """
        发送 GET 请求，处理所有可能的错误。
        - 网络错误（超时/连接失败）→ 重试
        - 5xx 错误 → 重试
        - 4xx 错误 → 不重试，打印错误信息
        - 全部重试失败 → 返回 None
        """
        # 你的代码
        url = f"{self.base_url}{path}"
        # try:
        #    req = requests.get(url,params=params,timeout=5)
        #    req.raise_for_status()
        #    return req.json()
        # except requests.exceptions.Timeout:
        #     print("超时，开始重试")
        #     for retry in range(self.max_retries + 1):
        #         req = requests.get(url, params=params, timeout=5)
        #         req.raise_for_status()
        #         if retry == self.max_retries:
        #             return None
        #         time.sleep(0.5)#
        #     # return req.json()
        # except requests.exceptions.ConnectionError:
        #    print("连接失败，开始重试")
        #    for retry in range(self.max_retries + 1):
        #        req = requests.get(url, params=params, timeout=5)
        #        req.raise_for_status()
        #        if retry == self.max_retries:
        #            return None
        #    # return req.json()
        # except requests.exceptions.HTTPError as err:
        #    if err.response.status_code >=500:
        #        print("服务器问题，开始重试")
        #        for retry in range(self.max_retries + 1):
        #            req = requests.get(url, params=params, timeout=5)
        #            req.raise_for_status()
        #            if retry == self.max_retries:
        #                return None
        #        return req.json()
        #    else:
        #        print(err)
        #        return None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.get(url, params=params or {}, timeout=self.timeout)
                response.raise_for_status()
                return response.json()

            except (requests.exceptions.Timeout,
                    requests.exceptions.ConnectionError) as e:
                print(f"[重试 {attempt}/{self.max_retries}] 网络错误: {type(e).__name__}")
                if attempt == self.max_retries:
                    return None
                time.sleep(1)

            except requests.exceptions.HTTPError as e:
                status = e.response.status_code
                if status >= 500:
                    print(f"[重试 {attempt}/{self.max_retries}] 服务器错误 {status}")
                    if attempt == self.max_retries:
                        return None
                    time.sleep(1)
                else:
                    print(f"[客户端错误 {status}] 请求有误，不重试")
                    return None

            except (ValueError, Exception) as e:
                print(f"[错误] {type(e).__name__}: {e}")
                return None

        return None



# 测试
client = SafeAPIClient("https://api.github.com")
user = client.get("/users/torvalds")
if user:
    print(f"用户: {user['login']}")