# 1

def get_first(s: str) -> int:
    for l in s:
        if l.isnumeric():
            return int(l)

def get_last(s: str) -> int:
    for i in range(len(s)-1, -1, -1):
        if s[i].isnumeric():
            return int(s[i])

def get_number(s: str) -> int:
    return get_first(s) * 10 + get_last(s)

def solution(arr: list) -> int:
    return sum(map(get_number, arr))

with open("./data.txt") as f:
    data1 = list(map(lambda line: line.strip(), f.readlines()))
    print(solution(data1))


# 2


numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def numberify_first(s: str, numbers: dict) -> str:
    for i in range(len(s)):
        for n in numbers.keys():
            if s[i:].startswith(n):
                s = s.replace(n, numbers[n], 1)
                return s
    return s


def numberify_last(s: str, numbers: dict) -> str:
    for i in range(len(s)-1, -1, -1):
        for n in numbers.keys():
            if s[i:].startswith(n):
                s = s.replace(n, numbers[n])
                return s
    return s


with open("./data.txt") as f:
    data2 = list(map(lambda line: numberify_last(numberify_first(line.strip().lower(), numbers), numbers), f.readlines()))
    print(data2)
    print(solution(data2))


