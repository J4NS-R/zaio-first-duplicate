
def firstDupe(a):
    """Finds the first duplicate in a list @ O(n)"""
    passed = {}

    for i in a:
        if i in passed:  # O(1)
            return i
        else:
            passed[i] = True

    return -1


if __name__ == '__main__':

    print(
        firstDupe([2, 1, 3, 5, 3, 2])
    )
