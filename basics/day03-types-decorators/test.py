# 代码阅读题
def process(value: int, multiplier: float = 2.0) -> str:
    return str(value * multiplier)

print(process(5))            # 输出 A 10.0
print(process(3, 1.5))       # 输出 B 4.5
print(process("hello", 3))   # 输出 C hellohellohello
print(process(10, "2"))      # 输出 D 20.0
## print(process(10, "2"))  2222222222 只要有一个是str就是重复

from functools import wraps

def upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("upper: before")
        result = func(*args, **kwargs)
        print("upper: after")
        return result.upper()
    return wrapper

def star(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("star: before")
        result = func(*args, **kwargs)
        print("star: after")
        return f"*{result}*"
    return wrapper

@upper
@star
def greet(name: str) -> str:
    print(f"greet: {name}")
    return f"hello {name}"

result = greet("world")
print(f"result: {result}")
# upper（star（greet(“world”)））
## upper wrapper → star wrapper → 原始 greet
# greet: world
# star: before
# greet: world
# hello world
# star: after
# upper: before
# hello hello world
# upper: after
# HELLO HELLO WORLD
## 写错
# upper: before
## 执行 result = func(*args, **kwargs)
## 这里 upper 的 func = star 包装后的函数，进入 star wrapper
# star: before
# greet: world
# star: after
# upper: after
# result: *HELLO WORLD*

from functools import wraps

def repeat(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

result = say_hello("Python")
print(len(result))        # 输出 A 3
print(result[0])          # 输出 B hello，python！
print(result[-1])         # 输出 C hello，hello，hello，python
#Hello, Python! 循环调用 不会改变参数
print(say_hello.__name__) # 输出 D say_hello

#代码纠错
# def log_calls(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         func(*args, **kwargs)  # 错误 1
#         print(f"Done {func.__name__}")
#     return wrapper  # 错误 2 不在这一行，在别处
#
# @log_calls
# def add(a: int, b: int) -> int:
#     return a + b
#
# result = add(3, 5)
# print(f"result = {result}")  # 期望输出 8，但实际输出 None
from functools import wraps
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        re = func(*args, **kwargs)  # 错误 1
        print(f"Done {func.__name__}")
        return re
    return wrapper
@log_calls
def add(a: int, b: int) -> int:
    return a + b
result = add(3, 5)
print(f"result = {result}")

# def find_user(user_id: str, active_only: str = True) -> list:
#     """根据 ID 查找用户"""
#     users = {
#         1: {"name": "Alice", "active": True},
#         2: {"name": "Bob", "active": False},
#     }
#     user = users.get(user_id)
#     if user is None:
#         return None
#     if active_only and not user["active"]:
#         return None
#     return user

# 输出考虑不全面 def find_user(user_id: int, active_only: bool= True) -> dict:
def find_user(user_id: int, active_only: bool = True) -> dict | None:
    """根据 ID 查找用户"""
    users = {
        1: {"name": "Alice", "active": True},
        2: {"name": "Bob", "active": False},
    }
    user = users.get(user_id)
    if user is None:
        return None
    if active_only and not user["active"]:
        return None
    return user

#实战编程题
from functools import wraps
def cache(func):
    """缓存函数结果，相同参数不重复计算"""
    # 你的代码
    histry = {}
    @wraps(func)
    def memory(*args, **kwargs):
        # 不能写在这，作用域导致任何数进入result都是空字典histry = {}
        if args[0] not in histry:
            result = func(*args, **kwargs)
            histry[args[0]] = result
        else:
            result = histry[args[0]]
        return result
    return memory

@cache
def expensive_calculation(n: int) -> int:
    print(f"  计算 {n}...")  # 只在未缓存时打印
    return n * n

print(expensive_calculation(5))   # 计算 5... → 25
print(expensive_calculation(5))   # 直接返回 25（不打印"计算"）
print(expensive_calculation(3))   # 计算 3... → 9

current_user = {"name": "zj", "role": "admin"}
def require_role(role: str):
    """检查用户角色，无权限则拒绝"""
    # 你的代码
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user["role"] == role:
                return func(*args, **kwargs)
            else:
                return "权限不足：需要 admin 角色"
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user_id: int) -> str:
    return f"已删除用户 {user_id}"

@require_role("admin")
def view_stats() -> dict:
    return {"total_users": 100, "active": 85}

print(delete_user(42))   # 当前用户是 admin，允许 → "已删除用户 42"

current_user["role"] = "viewer"
print(delete_user(42))   # 现在是 viewer，拒绝 → "权限不足：需要 admin 角色"
