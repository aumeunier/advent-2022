from common import parse


def process_signal(filename):
    inputs = parse(filename)
    x = 1
    result = 0
    cycles = 1
    next_cycle = 20
    crt_lines = []
    crt = ""
    for i in range(len(inputs)):
        input = inputs[i]
        if input == "noop":
            crt += "#" if x <= cycles % 40 <= x+2 else "."  # cycle-1
            print(
                f"Pixel is at {x}. {''.join([('#' if x-1 <= j <= x+1 else '.') for j in range(40)])}\nDrawing {cycles-1} => {crt[-1]}")
            print(crt)
            if len(crt) == 40:
                crt_lines.append(crt)
                crt = ""
            cycles += 1
            if (cycles >= next_cycle):
                result += x * next_cycle
                next_cycle += 40
            continue
        # Else => begin adding X
        _, value = input.split(" ")
        # During cycle 1
        crt += "#" if x <= cycles % 40 <= x+2 else "."  # cycle-1
        print(
            f"Pixel is at {x}. {''.join([('#' if x-1 <= j <= x+1 else '.') for j in range(40)])}\nDrawing {cycles-1} => {crt[-1]}")
        print(crt)
        if len(crt) == 40:
            crt_lines.append(crt)
            # print(crt)
            crt = ""
        cycles += 1
        if (cycles >= next_cycle):
            result += x * next_cycle
            next_cycle += 40
        # During cycle 2
        crt += "#" if x <= cycles % 40 <= x+2 else "."  # cycle-1
        print(
            f"Pixel is at {x}. {''.join([('#' if x-1 <= j <= x+1 else '.') for j in range(40)])}\nDrawing {cycles-1} => {crt[-1]}")
        print(crt)
        if len(crt) == 40:
            crt_lines.append(crt)
            # print(crt)
            crt = ""
        cycles += 1
        # Add X
        x += int(value)
        if (cycles >= next_cycle):
            result += x * next_cycle
            next_cycle += 40
    print(''.join(['-' for i in range(40)]))
    for crt in crt_lines:
        print(crt)
    print(f"Final X={x}, result={result}")
    return x, result


# x, result = process_signal("10-1")
# assert(x == -1)
# assert(result == 0)

x, result = process_signal("10-2")
assert(result == 13140)


x, result = process_signal("10-3")
