import collections
def commonChars(words):
    res = collections.Counter(words[0])
    for a in words:
        res &= collections.Counter(a)
    return list(res.elements())

A = ["bella","label","roller"]
print(commonChars(A))