def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return a ** 2 + b ** 2
    elif (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0):
        return (a + b) * 2
    else:
        return abs(a - b)
    return answer