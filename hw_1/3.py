import sys


def count_stats(file_object):
    lines_count = 0
    words_count = 0
    chars_count = 0
    for line in file_object:
        lines_count += 1
        words_count += len(line.split())
        chars_count += len(line.encode())
    return lines_count, words_count, chars_count


def print_stats(lines_num, words_num, chars_num, filename):
    if filename:
        print(f'{lines_num:8} {words_num:7} {chars_num:7} {filename}')
    else:
        print(f'{lines_num:8} {words_num:7} {chars_num:7}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        total_lines = 0
        total_words = 0
        total_chars = 0

        for idx, filename in enumerate(sys.argv[1:]):
            try:
                with open(filename, 'r') as file:
                    lines_num, words_num, chars_num = count_stats(file)
                    print_stats(lines_num, words_num, chars_num, filename)
                    total_lines += lines_num
                    total_words += words_num
                    total_chars += chars_num
            except FileNotFoundError:
                print(f"Ошибка: файл '{sys.argv[idx]}' не найден", file=sys.stderr)
                sys.exit(1)
        if len(sys.argv) > 2:
            print_stats(total_lines, total_words, total_chars, 'total')
    else:
        lines_num, words_num, chars_num = count_stats(sys.stdin)
        print_stats(lines_num, words_num, chars_num, None)
