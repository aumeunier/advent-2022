
def parse():
    with open('./files/day-2.txt') as f:
        lines = [line.strip().split(" ") for line in f.readlines()]
    return lines


def score_battle(other, me, indexes=["A", "B", "C"]):
    if other == me:
        return 3
    else:
        i_o, i_m = indexes.index(other), indexes.index(me)
        return 6 if i_m == i_o + 1 or i_o == 2 and i_m == 0 else 0


def score_letter(me, indexes=["A", "B", "C"]): return 1 + indexes.index(me)


def translate(move):
    return "Rock" if move == "A" else "Paper" if move == "B" else "Scissors"


def choose_move(opponent, result):
    match(result):
        case "X":  # must lose
            match(opponent):
                case "Rock": return "Scissors"
                case "Paper": return "Rock"
                case "Scissors": return "Paper"
        case "Y":  # must draw
            match(opponent):
                case "Rock": return "Rock"
                case "Paper": return "Paper"
                case "Scissors": return "Scissors"
        case "Z":  # must win
            match(opponent):
                case "Rock": return "Paper"
                case "Paper": return "Scissors"
                case "Scissors": return "Rock"


if __name__ == '__main__':
    lines = parse()
    total_score = 0
    # Round 1
    for l in lines:
        opponent, me = l
        me = me.replace("X", "A").replace("Y", "B").replace("Z", "C")
        total_score += score_battle(opponent, me) + score_letter(me)
    print(f"Score round 1: {total_score}")
    # Round 2
    total_score = 0
    for line in lines:
        # Translating for easier debugging
        indexes = ["Rock", "Paper", "Scissors"]
        opponent = translate(line[0])
        me = choose_move(opponent, line[1])
        total_score += score_battle(opponent, me, indexes) + score_letter(me, indexes)
    print(f"Score round 2: {total_score}")
