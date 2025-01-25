import multiprocessing
import random
import time
import concurrent.futures as c
import threading as t
from typing import Callable
from logic import Algorithm as s
from itertools import repeat


def run_times(data: list, timeout=5):
    times = []
    with c.ProcessPoolExecutor(max_workers=3) as executor:
        for each in executor.map(run_threaded_algorithm, repeat(data), s.ALGORITHMS, repeat(timeout)):
            times.append(each)

    return times


def run_threaded_algorithm(data: list, fn: Callable[[list], None], timeout: int):
    thread = t.Thread(target=fn.run_algorithm, args=(data,))
    time1 = time.perf_counter()
    thread.start()
    thread.join(timeout)
    time2 = time.perf_counter()
    if thread.is_alive():
        elapse = "Exceeded Time Limit"
    else:
        elapse = f"{time2 - time1:.3f}"
    return {"algorithm": fn.__class__.__name__, "time": elapse}


def time_table(times: list[dict], timeout: int):
    ph = "Timeout Value"
    print(f"  {ph:<18} |   {timeout}.00s")
    print("--------------------------------")
    for e in times:
        print(f"  {e['algorithm']:<18} |   {e['time']}s")


def main() -> None:
    random_data = [random.randint(0, 10000) for _ in range(10000)]
    times = run_times(random_data, 2)
    time_table(times, 2)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f" Time elapsed is {t2 - t1:.3f}")