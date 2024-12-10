import codecs
import logging
import time
from multiprocessing import Queue, Process, Pipe

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def rot13(s):
    return codecs.encode(s, "rot_13")


def process_a(from_main_to_a_queue, to_b_conn):
    while True:
        msg = from_main_to_a_queue.get()
        msg_lowered = msg.lower()
        logging.info(f'Процесс A: получено сообщение {msg} и сконвертировано в {msg_lowered}')
        to_b_conn.send(msg_lowered)
        time.sleep(5)


def process_b(from_a_conn, from_b_to_main_queue):
    while True:
        msg = from_a_conn.recv()
        encoded_msg = rot13(msg)
        logging.info(f'Процесс B: получено сообщение {msg} и сконвертировано в {encoded_msg}')
        from_b_to_main_queue.put(encoded_msg)


if __name__ == '__main__':
    from_main_to_a_queue = Queue()
    from_a_conn, to_b_conn = Pipe()
    from_b_to_main_queue = Queue()

    a = Process(target=process_a, args=(from_main_to_a_queue, to_b_conn))
    b = Process(target=process_b, args=(from_a_conn, from_b_to_main_queue))

    a.start()
    b.start()

    while True:
        msg = input('Введите сообщение для процесса А. Для остановки напишите exit:\n').strip()
        if msg.lower() == 'exit':
            break
        from_main_to_a_queue.put(msg)
        logging.info(f'Main: отправлено сообщение {msg}')
        res_msg = from_b_to_main_queue.get()
        logging.info(f'Main: получено сообщение {res_msg}')

    logging.info('Успешное завершение main процесса')

    a.terminate()
    b.terminate()
