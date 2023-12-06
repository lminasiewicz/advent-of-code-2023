def listmap(f, data: list) -> list:
   return list(map(f, data))


def transform_data(initial_data: list[str]) -> list[tuple[int, int]]:
    result = []
    times = listmap(int, [elem for elem in initial_data[0] if elem.isnumeric()])
    distances = listmap(int, [elem for elem in initial_data[1] if elem.isnumeric()])
    for i in range(len(times)):
        result.append((times[i], distances[i]))
    return result


def last(race: tuple[int, int]) -> int:
    for velocity in range(race[0], 0, -1):
        if (race[0] - velocity) * velocity > race[1]:
            return velocity


def first(race: tuple[int, int]) -> int:
    for velocity in range(race[0]+1):
        if (race[0] - velocity) * velocity > race[1]:
            return velocity


def get_range(race: tuple[int, int]) -> int:
    return last(race) - first(race) + 1


def solution(data: list[tuple[int, int]]) -> int:
    result = 1
    for race in data:
        result *= get_range(race)
    return result


if __name__ == "__main__":
    with open("./data.txt") as f:
        initial_data = listmap(lambda category: category.strip().split(" "), f.readlines())
        data = transform_data(initial_data)
        print(solution(data))