from binarySearch import search

def test1():
    arr = [1, 2, 3]
    result = search(arr, 2)
    assert result == 1
    
def test2():
    arr = [0, 2, 5, 6, 7]
    result = search(arr, 2)
    assert result == 1
    
def test3():
    arr = [0, 2, 5, 6, 7]
    result = search(arr, 0)
    assert result == 0

def test4():
    arr = [0, 2, 5, 6, 7]
    result = search(arr, 4)
    assert result == -1

def test5():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = search(arr, 7)
    assert result == 6

def test6():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = search(arr, 1)
    assert result == 0

def test7():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = search(arr, 10)
    assert result == 9

def test8():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = search(arr, 5)
    assert result == 4

def test9():
    arr = [2, 4, 6, 8, 10]
    result = search(arr, 8)
    assert result == 3

def test10():
    arr = [2, 4, 6, 8, 10]
    result = search(arr, 9)
    assert result == -1