import datetime
import time
from multiprocessing import Process, Queue


def work(p_id, s_num: int, e_num: int, result_queue: Queue):
    print(f"PID: {p_id}")

    total_num = 0
    for i in range(s_num, e_num):
        total_num += i
    result_queue.put(total_num)
    return


if __name__ == "__main__":
    start = 0
    end = 1000000000

    result = Queue()

    s_time = time.time()
    th1 = Process(target=work, args=(1, 1, end // 2, result))
    th2 = Process(target=work, args=(2, end // 2, end, result))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    e_time = time.time()
    sec = (e_time - s_time)
    result_time = datetime.timedelta(seconds=sec)
    print(f"Runtime sec: {result_time}")

    result.put("STOP")

    ttl = 0
    while True:
        tmp = result.get()
        if tmp == "STOP":
            break
        else:
            ttl += tmp

    print(f"Result: {ttl}")
