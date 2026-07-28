# 实现 `count_words(text: str) -> dict[str, int]`
# ，统计一段文本中每个单词出现的次数（忽略大小写）。练习 dict
def count_words(test: str) -> dict[str,int]:
    # counts = {}
    counts: dict[str, int] = {}#强制标注类型
    words = test.lower().split()
    for word in words:
        counts[word] = counts.get(word,0)+1
    return counts

print(count_words("Hello world hello Python"))

# 实现 `find_pairs(nums: list[int], target: int) -> list[tuple]`
# ，找出列表中所有和为 target 的不重复数对。练习 set

def find_pairs(nums: list[int], target: int) -> list[tuple]:
    # 集合seen：存放循环中已经遍历过的数字，用来快速查找互补数
    seen: set[int] = set()
    # 存放符合条件的数对，利用集合元素唯一性自动去重
    pairs = set()
    for num in nums:
        complement = target - num
        # 判断：互补数是否在之前遍历过的数字集合里
        if complement in seen:
            # 目的：(1,6) 和 (6,1) 统一变成 (1,6)，避免重复数对
            pair = tuple(sorted([num, complement]))
            pairs.add(pair)
        seen.add(num)
    return list(pairs)

print(find_pairs([1, 2, 3, 4, 5, 6], 7))
