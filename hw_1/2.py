import sys


def tail(file_object, num_lines: int):
    lines = file_object.readlines()[-num_lines:]
    for line in lines:
        print(line, end='')


def process_file(idx: int, filename: str, num_lines: int):
    try:
        with open(filename, 'r') as file:
            tail(file, num_lines)
            print()
    except FileNotFoundError:
        print(f"Ошибка: файл '{sys.argv[idx]}' не найден", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    num_lines_for_files = 10
    num_lines_for_stdin = 17

    if len(sys.argv) == 2:
        process_file(1, sys.argv[1], num_lines_for_files)
    elif len(sys.argv) > 2:
        for idx, filename in enumerate(sys.argv[1:]):
            print(f'==> {filename} <==')
            process_file(idx, filename, num_lines_for_files)
    else:
        tail(sys.stdin, num_lines_for_stdin)
