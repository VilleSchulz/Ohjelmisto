def interpolation_search(array, value, start=None, end=None):
    # Prepare the variables this way, so the user can call
    # the function with just the array and value to be searched.
    # If start and end are not defined, the search is conducted
    # in the whole array.
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    # Calculate a midpoint
    if array[start] == array[end]:  # Avoid division by zero
        return start if array[start] == value else None

    midpoint = start + int((end - start) * ((value - array[start]) / (array[end] - array[start])))

    # If the calculated midpoint is not within the search area, return
    if midpoint < start or midpoint > end:
        return None

    # If the value is found at the midpoint, return the index of midpoint
    if array[midpoint] == value:
        return midpoint

    # If the value being searched is smaller than the one in the midpoint
    # and there is at least one element left to the midpoint
    if value < array[midpoint] and midpoint >= start + 1:
        # Perform the search on the left part
        return interpolation_search(array, value, start=start, end=midpoint - 1)

    # If the value being searched is bigger than the one in the midpoint
    # and there is at least one element right to the midpoint
    if value > array[midpoint] and midpoint <= end - 1:
        # Perform the search on the right part
        return interpolation_search(array, value, start=midpoint + 1, end=end)

    return None


# Testidata
array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]

print(interpolation_search(array, 0))   # 0
print(interpolation_search(array, 98))  # 19
print(interpolation_search(array, 29))  # 6
print(interpolation_search(array, 100)) # None
print(interpolation_search(array, -1))  # None
print(interpolation_search(array, 4))   # None
