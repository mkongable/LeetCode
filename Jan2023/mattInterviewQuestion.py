# given a string, return the string with adjacent duplicates removed

def removeDuplicates(s):
    if len(s) == 0:
        return s
    prevChar = None
    result = ""
    for char in s:
        if char != prevChar:
            result += char
            prevChar = char
    return result


print(removeDuplicates("abccba"))