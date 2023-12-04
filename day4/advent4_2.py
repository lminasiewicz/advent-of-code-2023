import advent4_1 as pt1

# n^3 time complexity but hey it works

def find_card_by_id(data: list[dict], id: int) -> dict | None:
    for card in data:
        if card["id"] == id:
            new_card = card
            return new_card


def add_copies(data: list[dict], id: int, count: int):
    for new_id in range(id + 1, id + count + 1):
        new_card = find_card_by_id(data, new_id)
        if new_card:
            data.append(new_card)


def solution2(data: list[dict]) -> int:
    for card in data:
        add_copies(data, card["id"], pt1.match_cards(card))
    return len(data)


if __name__ == "__main__":
    with open("./data.txt") as f:
        data = pt1.transform_data(f.readlines())
        print(solution2(data))
    
