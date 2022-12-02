def part_1():
    with open("input_2.txt", "r") as file:
        lines = file.readlines()
        stack = 0
        res = None
        for line in lines:
            if line == "\n":
                if res is None or stack > res:
                    res = stack
                stack = 0
            else:
                stack += int(line)

    print(res)

# part 2

def part_2():
    with open("input_1.txt", "r") as file:
        lines = file.readlines()
        stack = 0
        top_3 = []
        res = None
        for line in lines:
            if line == "\n":
                top_3.append(stack)
                stack = 0
            else:
                stack += int(line)
    top_3.sort(reverse=True)
    print(sum(top_3[:3]))

part_2()
