from typing import List

def compress(chars: List[str]) -> int:

    def insertIterableAfterIdx(idx, iterable):
        for i in range(len(iterable) - 1, -1, -1):
            chars.insert(idx, iterable[i])

    prevChar = chars.pop()
    count = 1
    curIdx = len(chars) - 1
    while curIdx >= 0:
        if chars[curIdx] == prevChar:
            count += 1
            chars.pop(curIdx)
        else:
            if count > 1:
                insertIterableAfterIdx(curIdx + 1, list(str(count)))
                chars.insert(curIdx + 1, prevChar)
            else:
                chars.insert(curIdx + 1, prevChar)
            prevChar = chars[curIdx]
            chars.pop(curIdx)
            count = 1
        curIdx -= 1

    if count > 1:
        insertIterableAfterIdx(curIdx + 1, list(str(count)))
        chars.insert(curIdx + 1, prevChar)
    else:
        chars.insert(curIdx + 1, prevChar)
    return len(chars)

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))
print(chars)