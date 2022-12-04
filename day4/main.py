def part_1():
    def build_range(s):
        a, b = s.split("-")
        return list(range(int(a), int(b)+1))

    with open("input.txt", "r") as file:
        lines = file.readlines()
        
        res = 0
        for line in lines:
            line = line.replace("\n", "")
            elf_1, elf_2 = line.split(",")
            a = build_range(elf_1)
            b = build_range(elf_2)

            set_a = set(a)
            set_b = set(b)
            common = list(set_a & set_b)
            if common == a or common == b:
                res += 1

    print(res)


def part_1_1():
    def build_range(s):
        a, b = s.split("-")
        return list(range(int(a), int(b)+1))

    with open("test.txt", "r") as file:
        lines = file.readlines()
        
        res = 0
        for line in lines:
            line = line.replace("\n", "")
            elf_1, elf_2 = line.split(",")
            a_1, b_1 =[int(_)  for _ in elf_1.split("-")]
            a_2, b_2 =[int(_)  for _ in elf_2.split("-")]

            if a_1 >= a_2 and b_1 <= b_2:
                res += 1
            elif a_2 >= a_1 and b_2 <= b_1:
                res += 1
        print(res)



def part_2():
    def build_range(s):
        a, b = s.split("-")
        return set(list(range(int(a), int(b)+1)))

    with open("input.txt", "r") as file:
        lines = file.readlines()
        
        res = 0
        for line in lines:
            line = line.replace("\n", "")
            elf_1, elf_2 = line.split(",")
            set_1 = build_range(elf_1)
            set_2 = build_range(elf_2)
            if len(set_1 & set_2) > 0:
                res += 1

        print(res)

part_2()
