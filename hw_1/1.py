import sys


def hl(lines):
    for i, line in enumerate(lines):
        print(f'{i + 1:6d}\t{line}', end='')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as file:
                hl(file)
        except FileNotFoundError:
            print(f"Ошибка: файл '{sys.argv[1]}' не найден", file=sys.stderr)
            sys.exit(1)
    else:
        hl(sys.stdin)
