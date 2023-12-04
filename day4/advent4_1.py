def listmap(f, data: list) -> list:
   return list(map(f, data))


def list_strip(data: list) -> list:
    return [elem for elem in data if elem != ""]


def transform_data(data: list[str]) -> dict:
    data = listmap(lambda s: s.strip().split(":"), data)
    data = listmap(lambda l: {"id": int(l[0][5:]), "winning": l[1].split("|")[0].split(" "), "yours": l[1].split("|")[1].split(" ")}, data)
    return listmap(lambda d: {"id": d["id"], "winning": listmap(int, list_strip(d["winning"])), "yours": listmap(int, list_strip(d["yours"]))}, data)


def get_points(count: int) -> int:
    if count <= 0:
        return 0
    else:
        return 2**(count-1)


def match_cards(card: dict) -> int:
    count = 0
    for elem in card["yours"]:
        if elem in card["winning"]:
            count += 1
    return get_points(count)


def solution(data: list[dict]):
    points = []
    for card in data:
        points.append(match_cards(card))
    return sum(points)
    

if __name__ == "__main__":
    with open("./data.txt") as f:
        data = transform_data(f.readlines())
        print(solution(data))