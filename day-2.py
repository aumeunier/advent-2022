
def parse():
    with open('./files/day-2.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def score_round1(line):
    opponent, me = line.split(" ")
    score = 0
    match(me):
        case "X":
            score = 1
            match(opponent):
                case "A": score += 3
                case "B": score += 0
                case "C": score += 6
        case "Y":
            score = 2
            match(opponent):
                case "A": score += 6
                case "B": score += 3
                case "C": score += 0
        case "Z":
            score = 3
            match(opponent):
                case "A": score += 0
                case "B": score += 6
                case "C": score += 3
        case _: score = 0
    return score


def translate(
    move): return "Rock" if move == "A" else "Paper" if move == "B" else "Scissors"


def score(opponent, me):
    score = 0
    match(me):
        case "Rock":
            score = 1
            match(opponent):
                case "Rock": score += 3
                case "Paper": score += 0
                case "Scissors": score += 6
        case "Paper":
            score = 2
            match(opponent):
                case "Rock": score += 6
                case "Paper": score += 3
                case "Scissors": score += 0
        case "Scissors":
            score = 3
            match(opponent):
                case "Rock": score += 0
                case "Paper": score += 6
                case "Scissors": score += 3
        case _: score = 0
    return score


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
    for line in lines:
        opponent, res = line.split(" ")
        me = choose_move(translate(opponent), res)
        s = score(translate(opponent), me)
        total_score += s
    print(total_score)
