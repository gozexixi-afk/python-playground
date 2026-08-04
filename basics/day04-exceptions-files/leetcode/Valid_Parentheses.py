# 给定一个只包括
# '('，')'，'{'，'}'，'['，']'
# 的字符串
# s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
#
# 示例
# 1：
#
# 输入：s = "()"
#
# 输出：true
#
# 示例
# 2：
#
# 输入：s = "()[]{}"
#
# 输出：true
#
# 示例
# 3：
#
# 输入：s = "(]"
#
# 输出：false
#
# 示例
# 4：
#
# 输入：s = "([])"
#
# 输出：true
#
# 示例
# 5：
#
# 输入：s = "([)]"
#
# 输出：false
# https://leetcode.cn/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        standard = {")":"(","}":"{","]":"["}
        stack = []
        for char in s:
            if char  in standard.keys() and len(stack) == 0:
                return False
            elif char in standard.keys():
                if stack[len(stack)-1] == standard[char]:
                    stack.pop()
                    return True
                return False
            else:
                stack.append(char)
        if len(stack)!=0:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:  # s 长度必须是偶数
            return False
        mp = {')': '(', ']': '[', '}': '{'}
        st = []
        for c in s:
            if c not in mp:  # c 是左括号 mp默认是key
                st.append(c)  # 入栈
            elif not st or st.pop() != mp[c]:  # c 是右括号 not st栈为空
                return False  # 没有左括号，或者左括号类型不对
        return not st  # 所有左括号必须匹配完毕

