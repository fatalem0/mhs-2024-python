import argparse
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging
import math
from multiprocessing import cpu_count

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)


def integrate(args):
    f, start, end, n_iter = args
    acc = 0
    step = (end - start) / n_iter
    for i in range(n_iter):
        acc += f(start + i * step) * step
    return acc


def timer(f, a, b, *, n_jobs=1, n_iter=10000000, executor):
    chunk_size = (b - a) / n_jobs
    chunks = [(f, a + i * chunk_size, a + (i + 1) * chunk_size, n_iter // n_jobs)
              for i in range(n_jobs)]

    start_time = time.time()

    with executor(max_workers=n_jobs) as executor:
        results = executor.map(integrate, chunks)
        total = sum(results)

    end_time = time.time()
    execution_time = end_time - start_time

    logging.info(f"Total execution time with {n_jobs} {executor} workers: {execution_time:.4f} seconds")
    return total, execution_time


def run_test(executor):
    for n_jobs in range(1, cpu_count() * 2 + 1):
        timer(
            math.cos,
            0,
            math.pi / 2,
            n_jobs=n_jobs,
            n_iter=10000000,
            executor=executor,
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    args = parser.parse_args()

    if args.mode == 'thread_pool_executor':
        run_test(ThreadPoolExecutor)
    elif args.mode == 'process_pool_executor':
        run_test(ProcessPoolExecutor)
    else:
        raise RuntimeError('Invalid mode')
