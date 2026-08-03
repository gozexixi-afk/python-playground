# 用 Python 写 Two Sum，但要求：
# 1. 加完整的类型提示
# 2. 用装饰器给函数加上计时功能
# 3. 写至少 3 个 assert 测试 **assert 断言**：用来做代码自测
# import time
# def tow_sum (a: int | float, b: int | float) -> str:
#     # assert type(a) == int | float , "第一个参数必须为数字"
#     # assert type(b) == int | float , "第二个参数必须为数字"
#     start = time.time()
#     result = a + b
#     end = time.time()
#     time_taken = end - start
#     return str(f"计算结果是{result},花费{time_taken}")
#
# print(tow_sum(1945659, 46546))
#
# import time
# from functools import wraps


# 计时装饰器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[{func.__name__}] 耗时: {elapsed * 1000:.3f}ms")
        return result

    return wrapper


@timer
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    给定一个整数数组和一个目标值，找出和为目标值的两个数的索引。

    思路：用字典存 {目标值-当前值: 索引}，一次遍历搞定。
    时间复杂度：O(n)
    """
    seen: dict[int, int] = {}  # {需要的值: 索引}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# 测试
assert two_sum([2, 7, 11, 15], 9) == [0, 1], "基础测试失败"
assert two_sum([3, 2, 4], 6) == [1, 2], "相邻元素测试失败"
assert two_sum([3, 3], 6) == [0, 1], "相同元素测试失败"
assert two_sum([1, 2, 3], 10) == [], "无解测试失败"

print("所有测试通过！")