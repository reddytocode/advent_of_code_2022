def part_1():
    with open("input.txt", "r") as file:
    #with open("example.txt", "r") as file:
        lines = file.readlines()
        x = 0
        index = 0
        print(lines)
        lines = [line.replace("\n", "") for line in lines]
        for i in range(0, len(lines), 3):
            stack = lines[i:i+3]
            a, b, c = [set(_) for _ in stack]
            stack = []
            common = list(a & b & c )
            res = common[0]
            num = ord(res) - 96
            if num < 0:
                num += 58
            x += num

        print(x)

part_1()
