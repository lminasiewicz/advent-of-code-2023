def get_number(line: str, index: int) -> int | None:
    result = ""
    current = line[index]
    if current.isnumeric():
        result += current
        while index + 1 < len(line):
            index += 1
            current = line[index]
            if current.isnumeric():
                result += current
            else:
                break
        return int(result)


def symbol_is_valid(engine: list[str], lineindex: int, index: int) -> bool:
    if not engine[lineindex][index].isnumeric() and not engine[lineindex][index] == ".":
        return True
    else: return False 


def check_around(engine: list[str], lineindex: int, index: int) -> list[tuple[int, int]]:
    result = []
    for i in range(lineindex - 1, lineindex + 2):
        for j in range(index - 1, index + 2):
            if i >= 0 and i < len(engine) and j >= 0 and j < len(engine[lineindex]):
                if symbol_is_valid(engine, i, j):
                    result.append((i, j))
    return result


def adjacent_symbols(engine: list[str], lineindex: int, index: int) -> int | None:
    line = engine[lineindex]
    number = get_number(line, index)
    if number is not None:
        symbols = []
        for i in range(len(str(number))):
            for coords in check_around(engine, lineindex, index + i):
                if coords not in symbols:
                    symbols.append(coords)
        return len(symbols)


def solution(engine: list[str]):
    result = 0
    ignorechar = 0
    for lineindex in range(len(engine)):
        for index in range(len(engine[lineindex])):
            if ignorechar > 0:
                ignorechar -= 1
            else:
                symbol_count = adjacent_symbols(engine, lineindex, index)
                if symbol_count is not None and symbol_count > 0:
                    number = get_number(engine[lineindex], index)
                    result += number
                    ignorechar = len(str(number)) - 1
    return result

if __name__ == "__main__":
    with open("./data.txt") as f:
        data = list(map(lambda line: line.strip(), f.readlines()))
        print(solution(data))