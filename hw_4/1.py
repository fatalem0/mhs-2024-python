import argparse
from multiprocessing import Process
import timeit
from threading import Thread


def fibonacci(n):
    if n in {0, 1}:
        return n

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number
    return fib_number


def fibonacci_sync(n, times):
    for _ in range(times):
        fibonacci(n)


def fibonacci_with_primitive(n, primitives_num, primitive):
    spawned_primitives: list = []
    for _ in range(primitives_num):
        spawned = primitive(target=fibonacci, args=(n,))
        spawned_primitives.append(spawned)
        spawned.start()

    for spawned in spawned_primitives:
        spawned.join()


def fibonacci_with_thread(n, primitives_num):
    fibonacci_with_primitive(n, primitives_num, Thread)


def fibonacci_with_process(n, primitives_num):
    fibonacci_with_primitive(n, primitives_num, Process)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('number')
    parser.add_argument('-pn', '--primitives-number')
    parser.add_argument('-m', '--mode')

    args = parser.parse_args()

    if args.mode == 'process':
        time = timeit.timeit(f"fibonacci_with_process({args.number}, {args.primitives_number})",
                             setup="from __main__ import fibonacci_with_process")
        print(
            f'Время выполнения при использовании процессов для нахождения числа Фибоначчи для числа {args.number}: {time}')
    elif args.mode == 'thread':
        time = timeit.timeit(f"fibonacci_with_thread({args.number}, {args.primitives_number})",
                             setup="from __main__ import fibonacci_with_thread")
        print(
            f'Время выполнения при использовании потоков для нахождения числа Фибоначчи для числа {args.number}: {time}')
    elif args.mode == 'sync':
        time = timeit.timeit(f"fibonacci_sync({args.number}, {args.primitives_number})",
                             setup="from __main__ import fibonacci_sync")
        print(f'Время выполнения при синхронном запуске для нахождения числа Фибоначчи для числа {args.number}: {time}')
    else:
        raise RuntimeError('Invalid mode')
