def listmap(f, data: list) -> list:
   return list(map(f, data))


def is_label(s: str) -> bool:
   if s[0].isalpha():
      return True
   else:
      return False


def transform_data(data: list[list[str]]) -> dict:
    result = {}
    current = ""
    for elem in data:
        if is_label(elem[0]):
            result[elem[0][:-5]] = []
            current = elem[0][:-5]
        else:
            result[current].append(listmap(int, elem[0].split(" ")))
    return result


def map_through(entry: int, m: list[list[int]]) -> int:
    larger = 0
    for elem in m:
        if entry >= elem[1] and entry <= elem[1] + elem[2]:
            return elem[0] + (entry - elem[1])
        elif entry >= elem[1] + elem[2]:
            larger += elem[2]
    return entry
      


def seed_to_location(seed: int, data: dict) -> int:
   soil = map_through(seed, data["seed-to-soil"])
   fertilizer = map_through(soil, data["soil-to-fertilizer"])
   water = map_through(fertilizer, data["fertilizer-to-water"])
   light = map_through(water, data["water-to-light"])
   temperature = map_through(light, data["light-to-temperature"])
   humidity = map_through(temperature, data["temperature-to-humidity"])
   return map_through(humidity, data["humidity-to-location"])


def solution(seeds: list[int], data: dict) -> int:
    result = []
    for seed in seeds:
        result.append(seed_to_location(seed, data))
    return min(result)

if __name__ == "__main__":
    with open("./data.txt") as f:
        data = [elem for elem in listmap(lambda line: listmap(lambda elem: elem.strip(), line.split("\n\n")), f.readlines()) if elem != ['']]
        seeds = listmap(int, data[1][0].split(" "))
        data = transform_data(data[2:])
        print(solution(seeds, data))