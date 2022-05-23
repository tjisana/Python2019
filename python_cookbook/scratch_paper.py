from collections import deque


def search(lines, pattern, history=5):
    """search function yielding found pattern plus previous 5 lines"""
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open('somefile.txt') as f:
        for line, prev in search(f, 'python', 5):
            for pline in prev:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
