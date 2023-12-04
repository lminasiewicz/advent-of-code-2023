from advent4_1 import *

if __name__ == "__main__":
    with open("./data.txt") as f:
        data = transform_data(f.readlines())
        print(solution(data))