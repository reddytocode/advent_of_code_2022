def part_1():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        total = 0
        dic = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
        values = {"rock": 1, "paper": 2, "scissors": 3}
        for line in lines:
            line = line.split("\n")[0]
            me = 0
            x, y = line.split(" ")
            x = dic[x]
            y = dic[y]
            me += values[y]
            # me win
            win, draw, lost = False, False, False
            if x == "rock":
                if y == "rock":
                    draw = True
                elif y == "paper":
                    win = True
                else:
                    lost = True
            elif x == "paper":
                if y == "rock":
                    lost = True
                elif y == "paper":
                    draw = True
                else:
                    win = True
            elif x == "scissors":
                if y == "rock":
                    win = True
                elif y == "paper":
                    lost = True
                else:
                    draw = True
            if win:
                me += 6
            elif draw:
                me += 3

            total += me

    print(total)



def part_2():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        total = 0
        dic = {"AX": 3, "AY": 1, "AZ": 2, "BX": 1, "BY": 2, "BZ": 3, "CX": 2, "CY": 3, "CZ": 1}
        values = {"X": 0, "Y": 3, "Z": 6}

        for line in lines:
            line = line.split("\n")[0]
            me = 0
            x, y = line.split(" ")
            me += values[y]
            me += dic[f"{x}{y}"]

            total += me
        print(total)

part_2()
