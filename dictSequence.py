def isAlienSorted(words, order):
    orderMap = {}
    for i, char in enumerate(order):
        orderMap[char] = i + 1
    orderMap[''] = 0

    def compare(str1, str2):
        for i, j in zip(str1, str2):
            if orderMap[i] > orderMap[j]:
                return False
            elif orderMap[i] < orderMap[j]:
                return True
            else:
                continue
        return True if len(str1) <= len(str2) else False

    for i in range(len(words) - 1):
        if compare(words[i], words[i + 1]) == False:
            return False
    return True

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order))
