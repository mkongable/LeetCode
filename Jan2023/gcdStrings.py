def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    # Determine base unit of the string repeats
    # Determine if the base unit is a substring of both strings
    # Determine if the base unit can be repeated a number of times to make both strings
    # If it is, return the base unit
    # If it is not, return ""
    baseUnit = ""
    # break strings into chunks of the same size until every chunk is the same
    # if the chunk is the same, it is a base unit
    # if the chunk is not the same, it is not a base unit
    chunk = 1
    while chunk <= len(str1) and chunk <= len(str2):
        if len(str1) % chunk == 0 and len(str2) % chunk == 0:
            if str1[:chunk] == str2[:chunk]:
                baseUnit = str1[:chunk]
        chunk += 1
    # if baseUnit is not empty, check if it is a substring of both strings
    if baseUnit != "":
        if str1.count(baseUnit) * len(baseUnit) == len(str1) and str2.count(baseUnit) * len(baseUnit) == len(str2):
            return baseUnit
        else:
            return ""
        
string1 = "ABCDABCDABCDABCDACBD"
string2 = "ABCD"
print(gcdOfStrings(string1, string2))