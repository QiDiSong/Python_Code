import functools
def compare(str1, str2):
    for i, j in zip(str1, str2):
        if i < j:
            return -1
        elif i > j:
            return 1
        else:
            continue
    return -1 if (len(str1) <= len(str2)) else 1
ans = ["yes","is","hello","apple"]
ans_ = sorted(ans, key=functools.cmp_to_key(compare))
print(sorted(ans, key=functools.cmp_to_key(compare)))
