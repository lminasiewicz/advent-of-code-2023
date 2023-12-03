from advent3_1 import get_number

def check_around(engine: list[str], lineindex: int, index: int) -> list[tuple[int, int]]:
    result = []
    for i in range(lineindex - 1, lineindex + 2):
        for j in range(index - 1, index + 2):
            if i >= 0 and i < len(engine) and j >= 0 and j < len(engine[lineindex]):
                if symbol_is_valid(engine, i, j):
                    result.append((i, j))
    return result

def symbol_is_valid(engine: list[str], lineindex: int, index: int) -> bool:
    if engine[lineindex][index].isnumeric():
        return True
    else: return False


def adjacent_numbers(engine: list[str], lineindex: int, index: int) -> list[tuple[int, int]] | None:
    if engine[lineindex][index] == "*":
        numbers = []
        for coords in check_around(engine, lineindex, index):
            numbers.append(coords)
        return numbers


def find_start(engine: list[str], coord: tuple[int, int]) -> tuple[int, int]:
    start = coord[1]
    while start >= 0:
        if engine[coord[0]][start].isnumeric():
            start -= 1
        else:
            break
    return (coord[0], start)


def get_numbers_from_coords(engine: list[str], coords: list[tuple[int, int]]) -> list[int]:
    for index in range(len(coords)):
        coords[index] = find_start(engine, coords[index])
    starts = list(dict.fromkeys(coords))
    result = []
    for coord in starts:
        result.append(get_number(engine[coord[0]], coord[1]+1))
    return result


def product(l: list) -> int:
    if len(l) == 0:
        return 0
    else:
        result = 1
        for elem in l:
            result *= elem
        return result


def solution2(engine: list[str]):
    result = []
    for lineindex in range(len(engine)):
        for index in range(len(engine[lineindex])):
            instances = adjacent_numbers(engine, lineindex, index)
            if instances is not None:
                start_coords = list(map(lambda coord: find_start(engine, coord), instances))
                numbers = get_numbers_from_coords(engine, start_coords)
                if len(numbers) == 2:
                    result.append(numbers)
    return sum(list(map(product, result)))


if __name__ == "__main__":
    with open("./data.txt") as f:
        data = list(map(lambda line: line.strip(), f.readlines()))
        print(solution2(data))