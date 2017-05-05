"""
Given a sorted list of distinct integers, write a function that returns whether
there are two integers in the list that add up to 0. For example, you would
return true if both -14435 and 14435 are in the list, because
-14435 + 14435 = 0. Also return true if 0 appears in the list.
"""

from collections import Counter

def sum_finder(li):
    if li:  # to week out those tricky empty lists.
        new_li = [abs(num) for num in li]
        if Counter(new_li).most_common(1)[0][1] == 2:
            return True
        else:
            return 0 in li
    else:
        return False
