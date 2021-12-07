def solution(x, y):
    result = (1 + x) * x / 2
    if y > 1:
        result += (x + x + y - 2) * (y - 1) / 2

    return str(int(result))


print(solution(3, 2))
print(solution(5, 10))
