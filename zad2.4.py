import math
import multiprocessing

def compute_chunk(xs):
    return [math.cos(x) + math.log(x + 1) ** 2 for x in xs]

if __name__ == "__main__":
    print("2.4 test:")
    xs = [i * 0.01 for i in range(1, 10001)]
    workers = max(2, min(4, multiprocessing.cpu_count()))
    chunks = [xs[i::workers] for i in range(workers)]

    with multiprocessing.Pool(workers) as p:
        parts = p.map(compute_chunk, chunks)

    values = []
    for part in parts:
        values.extend(part)

    print("liczba punktów:", len(xs))
    print("pierwsze 5:", values[:5])
    print("ostatnie 5:", values[-5:])
