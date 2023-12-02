# 1

def get_id(game: str) -> int:
    return int(game[5:])


def group_colors(game: str) -> dict:
    red, green, blue = 0, 0, 0
    
    game = game.split(";")
    game = list(map(lambda pick: pick.split(","), game))
    game = list(map(lambda pick: list(map(lambda color: color.strip().split(" "), pick)), game))
    for pick in game:
        for col in pick:
            if col[1] == "red":
                red = max(red, int(col[0]))
            elif col[1] == "green":
                green = max(green, int(col[0]))
            elif col[1] == "blue":
                blue = max(blue, int(col[0]))
    
    return {"red": red, "green": green, "blue": blue}


def transform_data(data: list) -> list:
    games_separated = list(map(lambda game: game.split(":"), data))
    no_whitespace = list(map(lambda game: [game[0].strip(), game[1].strip()], games_separated))

    def transform_game(game):
        return {"id": get_id(game[0]), "colors": group_colors(game[1])}

    return list(map(transform_game, no_whitespace))


def is_possible(game: dict, color_data: dict) -> bool:
    if game["colors"]["red"] <= color_data["red"] and game["colors"]["green"] <= color_data["green"] and game["colors"]["blue"] <= color_data["blue"]:
        return True
    else: 
        return False


def solution(data: list, color_data: dict) -> int:
    """uses transformed data from transform_data. color_data is {"red": int, "green": int, "blue": int} which is 12, 13, 14 in ex.1."""
    result = 0
    for game in data:
        if is_possible(game, color_data):
            result += game["id"]
    return result


with open("./data.txt") as f:
    data1 = transform_data(list(map(lambda line: line.strip().lower(), f.readlines())))
    print(solution(data1, {"red": 12, "green": 13, "blue": 14}))





# 2

def get_power(colors: dict) -> int:
    return colors["red"] * colors["green"] * colors["blue"]

def solution2(data: list) -> int:
    """uses transformed data from transform_data."""
    result = list(map(lambda game: get_power(game["colors"]), data))
    return sum(result)

with open("./data.txt") as f:
    data2 = transform_data(list(map(lambda line: line.strip().lower(), f.readlines())))
    print(solution2(data2))
    