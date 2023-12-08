import advent7_1 as pt1


def determine_type(hand: tuple[str, int]) -> str:
    elements = []
    highest = (".", 0)
    second_highest = (".", 0)
    for i in range(5):
        elements.append((hand[0][i], 0))
    for i in range(len(elements)):
        for elem in elements:
            if elements[i][0] == elem[0]:
                elements[i] = (elements[i][0], elements[i][1] + 1)
    for elem in elements:
        if elem[1] > highest[1]:
            highest = (elem[0], elem[1])
    for elem in elements:
        if elem[1] > second_highest[1] and elem[0] != highest[0]:
            second_highest = (elem[0], elem[1])
    if highest[0] == "J":
        highest = (second_highest[0], second_highest[1] + highest[1])
        second_highest = ("J", 0)
    else:
        for i in range(len(elements)):
            if elements[i][0] == "J":
                highest = (highest[0], highest[1] + elements[i][1])
                break
    
    return pt1.assign_type_name(highest[1], second_highest[1])


def sort_data(data: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    key = {"HC": 0, "1P": 1, "2P": 2, "3": 3, "FH": 4, "4": 5, "5": 6}
    key2 = {"J": -1, "2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "Q": 10, "K": 11, "A": 12}
    return sorted(data, key=lambda hand: (key[hand[0]], key2[hand[1][0]], key2[hand[1][1]], key2[hand[1][2]], key2[hand[1][3]], key2[hand[1][4]]))


def assign_rank(data: list[tuple[str, str, int]]) -> list[tuple[int, str, str, int]]:
    sorted_data = sort_data(data)
    assigned_data = []
    for i in range(len(sorted_data)):
        assigned_data.append((i + 1, sorted_data[i][0], sorted_data[i][1], sorted_data[i][2]))
    return assigned_data


def transform_data(data: list[list[str]]) -> list[tuple[str, str, int]]:
    data = pt1.listmap(lambda hand: (hand[0], int(hand[1])), data)
    data = pt1.listmap(lambda hand: (determine_type(hand), hand[0], hand[1]), data)
    return data


if __name__ == "__main__":
    with open("./data.txt") as f:
        data = pt1.listmap(lambda category: category.strip().split(" "), f.readlines())
        data = assign_rank(transform_data(data))
        print(pt1.solution(data))