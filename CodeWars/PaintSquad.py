def paint_letterboxes(start, finish):
    result = [0] * 10
    for number in range(start, finish + 1):
        for digit in str(number):
            result[int(digit)] += 1
    return result