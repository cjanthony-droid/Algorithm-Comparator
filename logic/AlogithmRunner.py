import copy as copy
import time
import random

from logic.Algorithm import ALGORITHMS


def run_times(array: list, timeout=5):
    times = []
    for fn in ALGORITHMS:
        data = copy.deepcopy(array)
        elapse = timer(fn.run_algorithm, data)
        times.append({"algorithm": fn.__class__.__name__, "time":elapse})
    return times


def time_table(times: list[dict], timeout: int):
    ph = "Timeout Value"
    print(f"  {ph:<18} |   {timeout}.00s")
    print("--------------------------------")
    for e in times:
        print(f"  {e['algorithm']:<18} |   {e['time']}s")


def timer(fn, data: list) -> str:
    t1 = time.perf_counter()
    output = fn(data)
    t2 = time.perf_counter()
    elapse = f"{t2 - t1:.3f}"
    return elapse


def main() -> None:
    random_data = [random.randint(0, 10000) for _ in range(1000)]
    time_table(run_times(random_data), 5)


if __name__ == "__main__":
    main()

