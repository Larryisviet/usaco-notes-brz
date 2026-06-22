def lucky_sum(a, b, c):
    total = 0

    for num in [a, b, c]:
        if num == 13:
            break
        total += num

    return total
