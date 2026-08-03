import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] 执行耗时：{end - start:.2f} 秒")
        return result
    return wrapper

@timer
def slow_add(a: int, b: int) -> int:
    time.sleep(1)
    return a + b

@timer
def fast_multiply(a: int, b: int) -> int:
    return a * b

result1 = slow_add(3, 5)      # [slow_add] 执行耗时：1.00 秒 → 结果：8
result2 = fast_multiply(3, 5) # [fast_multiply] 执行耗时：0.00 秒 → 结果：15

def wrapper(*args, **kwargs):
    print(f"位置参数：{args}")      # 元组
    print(f"关键字参数：{kwargs}")   # 字典

wrapper(1, 2, 3)          # args=(1,2,3), kwargs={}
wrapper(a=1, b=2)          # args=(), kwargs={'a':1, 'b':2}
wrapper(1, 2, name="goze")  # args=(1,2), kwargs={'name':'goze# '}
import time

def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第 {attempt}/{max_attempts} 次失败: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_api(url: str) -> str:
    import random
    if random.random() < 0.7:
        raise ConnectionError("连接失败")
    return f"成功: {url}"

try:
    print(unreliable_api("https://api.example.com"))
except ConnectionError:
    print("所有重试都失败了")