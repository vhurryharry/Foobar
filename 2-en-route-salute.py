
def solution(s):
    toRight = 0
    total = 0

    for step in s:
        if step == '>':
            toRight += 1
        elif step == '<':
            total += toRight * 2

    return total


print(solution('>----<'))
print(solution('<<>><'))
