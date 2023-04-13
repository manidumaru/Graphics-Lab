from random import sample
from time import time_ns
from search import linear_search, binary_search

def run(n):
    data = sample(range(1, n*10000), n)
    data = sorted(data)
    
    # print(data)
    start_time = time_ns()
    linear_search(data, data[-1])
    # binary_search(data, data[-1], 0, len(data))
    end_time = time_ns()

    total_time = end_time - start_time
    print(f"{n} data = {total_time} nanoseconds")
    


if __name__ == "__main__":
    for i in range(1,7):
        n = 1000000 * i
        run(n)


