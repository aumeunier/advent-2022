from common import parse


def find_start(signal, l=4):
    for i in range(len(signal)):
        if len(set(signal[i:i+l])) == l:
            return i+l


print(find_start(parse(6)[0], 14))
