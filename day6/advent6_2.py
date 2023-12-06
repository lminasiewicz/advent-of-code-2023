import advent6_1 as pt1
import re

def transform_data2(initial_data: list[str]) -> tuple[int, int]:
    time = int(re.sub(", ", "", str(pt1.listmap(int, [elem for elem in initial_data[0] if elem.isnumeric()]))[1:-1]))
    distance = int(re.sub(", ", "", str(pt1.listmap(int, [elem for elem in initial_data[1] if elem.isnumeric()]))[1:-1]))
    return (time, distance)

solution2 = pt1.get_range

if __name__ == "__main__":
    with open("./data.txt") as f:
        initial_data = pt1.listmap(lambda category: category.strip().split(" "), f.readlines())
        data = transform_data2(initial_data)
        print(solution2(data))