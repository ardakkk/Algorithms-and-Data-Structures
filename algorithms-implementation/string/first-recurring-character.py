"""
Fist recurring character
Given a string, return the first recurring letter that appears. If there are no recurring letters, return None

Example:
    Input: qqwertty
    Output: q

    Input: qwerty
    Output: None
"""

# Time: O(n)
# Space: O(n)
def first_recurring_chars(s):
    seen_so_far = set()

    for c in s:
        if c in seen_so_far:
            return c
        seen_so_far.add(c)

    return None

# Time: O(n)
# Space: O(1)
def first_recurring_chars2(s):
    fist_index = 0
    second_index = 1

    for _ in s:
        if s[fist_index] == s[second_index]:
            return s[second_index]
        fist_index += 1
        second_index += 1

    return None

print(first_recurring_chars2('qwertty'))
# t

print(first_recurring_chars('qwerty'))
# None
