import advent5_1 as pt1

def solution2(seeds: list[int], data: dict) -> int:
    start = 0
    smallest = pt1.seed_to_location(seeds[0], data)
    for n in seeds:
        if n % 2 == 0:
            start = n
        else:
            for seed in range(start, start + n):
                curr = pt1.seed_to_location(seed, data)
                if curr < smallest:
                    smallest = curr
    return smallest

if __name__ == "__main__":
    with open("./data.txt") as f:
        data = [elem for elem in pt1.listmap(lambda line: pt1.listmap(lambda elem: elem.strip(), line.split("\n\n")), f.readlines()) if elem != ['']]
        seeds = pt1.listmap(int, data[1][0].split(" "))
        data = pt1.transform_data(data[2:])
        print(solution2(seeds, data))